import json

j = '''
    {
        "a": 100,
        "b": [1, 2, 3],
        "c": "python",
        "d": {
            "e": 4,
            "f": 5.5
        }
    }
'''


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        print("decode:", type(arg), arg)
        return "a simple string object"


print(json.loads(j, cls=CustomDecoder))


print('#' * 52 + '  As you can see, whatever we return from the `decode` method is the **result** of calling `loads`.')
print('#' * 52 + '  So, we might want to intercept certain JSON strings, handling them in some custom way, '
                 '  and delegate back to the parent class if its not a string we want to handle ourselves -'
                 '  but its all or nothing:')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


j_points = '''
{
    "points": [
        [10, 20],
        [-1, -2],
        [0.5, 0.5]
    ]
}
'''

j_other = '''
{
    "a": 1,
    "b": 2
}
'''


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        if 'points' in arg:
            obj = json.loads(arg)
            return "parsing object for points"
        else:
            return super().decode(arg)


print(json.loads(j_points, cls=CustomDecoder))
print(json.loads(j_other, cls=CustomDecoder))

print('#' * 52 + '  So, lets implement the custom decoder now, assuming that `points` will be a top level node'
                 '  in the JSON object:')


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        if 'points' in obj:  # top level
            obj['points'] = [Point(x, y)
                             for x, y in obj['points']]
        return obj


print(json.loads(j_points, cls=CustomDecoder))
print(json.loads(j_other, cls=CustomDecoder))

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

import re
pattern = r'"_type"\s*:\s*"point"'

print('word1\tword2')

print(r'word1\tword2')

regexp = re.compile(pattern)


print(regexp.search('"a": 1'))

print(regexp.search('"_type": "point"'))
print(regexp.search('"_type"   : "point"'))

print('#' * 52 + '  Alternatively, if we dont want to compile it'
                 ' (if we only use it once, there is no real need to do so), we can do a search this way:')

print(re.search(pattern, '"_type"  :  "point"'))

print('#' * 52 + '  OK, now that we have a working regular expression pattern we can implement our custom JSON decoder.')


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            # we have at least one `Point'
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        # recursive function to find and replace points
        # received object could be a dictionary, a list, or a simple type
        if isinstance(obj, dict):
            # first see if this dictionary is a point itself
            if '_type' in obj and obj['_type'] == 'point':
                # could have used: if obj.get('_type', None) == 'point'
                obj = Point(obj['x'], obj['y'])
            else:
                # root object is not a point
                # but it could contain a sub-object which itself
                # is or contains a Point object
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj


j = '''
{
    "a": 100,
    "b": 0.5,
    "rectangle": {
        "corners": {
            "b_left": {"_type": "point", "x": -1, "y": -1},
            "b_right": {"_type": "point", "x": 1, "y": -1},
            "t_left": {"_type": "point", "x": -1, "y": 1},
            "t_right": {"_type": "point", "x": 1, "y": 1}
        },
        "rotate": {"_type" : "point", "x": 0, "y": 0},
        "interior_pts": [
            {"_type": "point", "x": 0, "y": 0},
            {"_type": "point", "x": 0.5, "y": 0.5}
        ]
    }
}
'''

print(json.loads(j))

from pprint import pprint
pprint(json.loads(j, cls=CustomDecoder))

print('#' * 52 + '  The `JSONDecoder` class also has arguments such as `parse_int`, '
                 ' `parse_float`, etc we saw in the previous lecture.')
print('#' * 52 + '  We can use those to define a custom `JSONEncoder` class if we wanted to - lets say we want to use'
                 ' `Decimals` instead of floats - just like before,')
print('#' * 52 + '   but instead of specifying this each and every time we calls `loads`, '
                 ' we can bundle this up into a custom decoder instead:')

from decimal import Decimal
CustomDecoder = json.JSONDecoder(parse_float=Decimal)

d = CustomDecoder.decode(j)
pprint(d)

print('#' * 52 + '  Of course, we can combine this with our custom decoder too:')


class CustomDecoder(json.JSONDecoder):
    base_decoder = json.JSONDecoder(parse_float=Decimal)

    def decode(self, arg):
        obj = self.base_decoder.decode(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            # we have at least one `Point'
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        # recursive function to find and replace points
        # received object could be a dictionary, a list, or a simple type
        if isinstance(obj, dict):
            # first see if this dictionary is a point itself
            if '_type' in obj and obj['_type'] == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                # root object is not a point
                # but it could contain a sub-object which itself
                # is or contains a Point object nested at some level
                # maybe another dictionary, or a list
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            # received a list - need to run each item through make_pts
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj


pprint(json.loads(j, cls=CustomDecoder))

print('#' * 52 + '  Its not evident that our `Point(x=0.5, y=0.5)` actually contains `Decimal` objects - '
                 '  that is really just the string representation - so lets just make sure they are indeed '
                 ' `Decimal` objects:')

result = json.loads(j, cls=CustomDecoder)
pt = result['rectangle']['interior_pts'][1]
print(type(pt.x), type(pt.y))

