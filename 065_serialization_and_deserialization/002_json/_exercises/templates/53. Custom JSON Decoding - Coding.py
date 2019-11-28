print('#' * 52 + '  Once again, the standard simple types such as strings, numbers (ints and floats), '
                 '  arrays, and objects with key/value pairs. ')
print('#' * 52 + '  JSON does not differentiate between mutable and immutable lists - '
                 '  so everything that is an array ([...]) in JSON will get decoded into a list object.')

j = '''
    {
        "name": "Python",
        "age": 27,
        "versions": ["2.x", "3.x"]
    }
'''

import json

print(json.loads(j))

print('#' * 52 + '  But what about other data types, such as a date for example. How can we handle that?')

p = '''
    {
        "time": "2018-10-21T09:14:00",
        "message": "created this json string"
    }
'''

print(json.loads(p))

print('#' * 52 + '  For example, suppose we have a JSON object where any object that contains'
                 '  the key/value pair `"objecttype": "datetime"` is guaranteed to contain another key'
                 '  called `"value"` containing a date time in the format %Y-%m-%dT%H:%M:%S. ')

p = '''
    {
        "time": {
            "objecttype": "datetime",
            "value": "2018-10-21T09:14:15"
            },
        "message": "created this json string"
    }
'''

d = json.loads(p)

print(d)

print('#' * 52 + '  We could now run through our dictionary (top level only, we will come back to that), '
                 '  and convert any datetime structures (schema) into actual datetime objects:')

from datetime import datetime

for key, value in d.items():
    if (isinstance(value, dict) and
        'objecttype' in value and
        value['objecttype'] == 'datetime'):
        d[key] = datetime.strptime(value['value'], '%Y-%m-%dT%H:%M:%S')

print(d)

print('#' * 52 + '  We can do this with other "custom" JSON schemas as well.')
print('#' * 52 + '  Lets say we have a JSON schema that will encode fractions using a `fraction` type indicator'
                 '  and associated keys `numerator` and `denominator` with integer values,')

j = '''
    {
        "cake": "yummy chocolate cake",
        "myShare": {
            "objecttype": "fraction",
            "numerator": 1,
            "denominator": 8
        }
    }
'''

d = json.loads(j)

print(d)

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

from fractions import Fraction

for key, value in d.items():
    if (isinstance(value, dict) and
        'objecttype' in value and
        value['objecttype'] == 'fraction'):
        numerator = value['numerator']
        denominator = value['denominator']
        d[key] = Fraction(numerator, denominator)

print(d)

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')


def custom_decoder(arg):
    print('decoding: ', arg)
    return arg


j = '''
    {
        "a": 1,
        "b": 2, 
        "c": {
            "c.1": 1,
            "c.2": 2,
            "c.3": {
                "c.3.1": 1,
                "c.3.2": 2
            }
        }
    }
'''

d = json.loads(j, object_hook=custom_decoder)

print('#' * 52 + '  As you can see it called our decoder three times, '
                 '  the value for the key `c.3`, the value for the key `c` and the root object itself.')

j = '''
    {
        "time": {
            "objecttype": "datetime",
            "value": "2018-10-21T09:14:15"
            },
        "message": "created this json string"
    }
'''


def custom_decoder(arg):
    if 'objecttype' in arg and arg['objecttype'] == 'datetime':
        return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
    else:
        return arg  # important, otherwise we lose anything that's not a date!


print('#' * 52 + '  Lets just see how it works as a plain function first:')

print(custom_decoder(dict(objecttype='datetime', value='2018-10-21T09:14:15')))
print(custom_decoder((dict(a=1))))
d = json.loads(j, object_hook=custom_decoder)
print(d)

print('#' * 52 + '  The nice thing about this approach, is our code is simpler, and this works for nested items too:')

j = '''
    {
        "times": {
            "created": {
                "objecttype": "datetime",
                "value": "2018-10-21T09:14:15"
                },
            "updated": {
                "objecttype": "datetime",
                "value": "2018-10-22T10:00:05"
                }
            },
        "message": "log message here..."
    }
'''

d = json.loads(j, object_hook=custom_decoder)

print(d)

print('#' * 52 + '  ')
print()
print()
print('#' * 52 + '  We can also extend this custom decoder to include other structures (schemas).')


def custom_decoder(arg):
    ret_value = arg
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            ret_value = datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            ret_value = Fraction(arg['numerator'], arg['denominator'])
    return ret_value


j = '''
    {
        "cake": "yummy chocolate cake",
        "myShare": {
            "objecttype": "fraction",
            "numerator": 1,
            "denominator": 8
        },
        "eaten": {
            "at": {
                "objecttype": "datetime",
                "value": "2018-10-21T21:30:00"
                },
            "time_taken": "30 seconds"
        }
    }
'''

d = json.loads(j, object_hook=custom_decoder)

print(d)

print('#' * 52 + '  ')
print()
print()
print('#' * 52 + '  We cant really use a generic single dispatch approach we took with the encoder though -'
                 '  the decoder always receives a dictionary, so we cant build it that way.')
print('#' * 52 + '  We still have the issue of custom objects and classes - how do we handle those?')
print('#' * 52 + '  Well, in pretty much the same way as before - '
                 '  the content of the JSON has to indicate that the object is of a certain "type", '
                 '  and we can then decode it ourselves.')


class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __repr__(self):
        return f'Person(name={self.name}, ssn={self.ssn})'


j = '''
    {
        "accountHolder": {
            "objecttype": "person",
            "name": "Eric Idle",
            "ssn": 100
        },
        "created": {
            "objecttype": "datetime",
            "value": "2018-10-21T03:00:00"
        }
    }
'''


def custom_decoder(arg):
    ret_value = arg
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            ret_value = datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            ret_value = Fraction(arg['numerator'], arg['denominator'])
        elif arg['objecttype'] == 'person':
            ret_value = Person(arg['name'], arg['ssn'])
    return ret_value


d = json.loads(j, object_hook=custom_decoder)

print(d)

print('#' * 52 + '  We could also provide our custom JSON encoder in the person class to serialize '
                 '  that class in the way we expect when deserializing, as we saw in an earlier video:')


class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __repr__(self):
        return f'Person(name={self.name}, ssn={self.ssn})'

    def toJSON(self):
        return dict(objecttype='person', name=self.name, ssn=self.ssn)


from decimal import Decimal


def make_decimal(arg):
    print('Received:', type(arg), arg)
    return Decimal(arg)


j = '''
    {
        "a": 100,
        "b": 0.2,
        "c": 0.5
    }
'''

d = json.loads(j, parse_float=make_decimal)

print(d)

print('#' * 52 + '  As you can see we have decimals in our dictionary, instead of floats.')
print('#' * 52 + '  Note also that the argument we receive is a string - it would make little sense for us to receive'
                 '  a float since our function is the one that wants to specifically handle converting '
                 '  a JSON string to some particular type.')
print('#' * 52 + '  We can also intercept handling of integers and those constant values I mentioned.')

j = '''
    {
        "a": 100,
        "b": Infinity
    }
'''

print(json.loads(j))


def make_int_binary(arg):
    print('Received:', type(arg), arg)
    return bin(int(arg))


def make_const_none(arg):
    print('Received:', type(arg), arg)
    return None


print(json.loads(j,
           parse_int=make_int_binary,
           parse_constant=make_const_none))

print('#' * 52 + '  Also, you should not specify both `object_hook` and `object_pairs_hook` - if you do, '
                 '  then the `object_pairs_hook` will be used and `object_hook` will be ignored.')

j = '''
    {
        "a": [1, 2, 3, 4, 5],
        "b": 100,
        "c": 10.5,
        "d": NaN,
        "e": null,
        "f": "python"
    }
'''


def float_handler(arg):
    print('float handler', type(arg), arg)
    return float(arg)


def int_handler(arg):
    print('int handler', type(arg), arg)
    return int(arg)


def const_handler(arg):
    print('const handler', type(arg), arg)
    return None


def obj_hook(arg):
    print('obj hook', type(arg), arg)
    return arg


def obj_pairs_hook(arg):
    print('obj pairs hook', type(arg), arg)
    return arg


print(json.loads(j))
print(json.loads(j,
           object_hook=obj_hook,
           parse_float=float_handler,
           parse_int=int_handler,
           parse_constant=const_handler
          ))

print(json.loads(j,
           object_pairs_hook=obj_pairs_hook,
           parse_float=float_handler,
           parse_int=int_handler,
           parse_constant=const_handler
          ))

print('#' * 52 + '  And if we specify both object hooks, then `object_hook` is basically ignored:')

print(json.loads(j,
           object_hook=obj_hook,
           object_pairs_hook=obj_pairs_hook,
           parse_float=float_handler,
           parse_int=int_handler,
           parse_constant=const_handler
          ))