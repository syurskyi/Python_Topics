d = {
    "name": {
        "first": "...",
        "last": "..."
    },
    "contact": {
        "phone": [
            {"type": "...", "number": "..."},
            {"type": "...", "number": "..."},
            {"type": "...", "number": "..."},
        ],
        "email": ["...", "...", "..."]
    },
    "address": {
        "line1": "...",
        "line2": "...",
        "city": "...",
        "country": "..."
    }
}


import json

d1 = {"a": 100, "b": 200}
d1_json = json.dumps(d1)
print(d1_json, type(d1_json))

print('#' * 52 + '  By the way, we can obtain a better looking JSON string by specifying'
                 '  an indent for the `dump` or `dumps` functions:')

print(json.dumps(d1, indent=2))

print('#' * 52 + '  And we can deserialize the JSON string:')

d2 = json.loads(d1_json)

print(d2, type(d2))
print(d1 == d2)

print('#' * 52 + '  There is a big caveat here.')
print('#' * 52 + '   In Python, keys can be any hashable object.')
print('#' * 52 + '  But remember that in JSON keys must be strings!')

d1 = {1: 100, 2: 200}

d1_json = json.dumps(d1)

print(d1_json)

print('#' * 52 + '  Notice how the keys are now strings in the JSON "object".')
print('#' * 52 + '  And when we deserialize:')

d2 = json.loads(d1_json)

print(d1)
print(d2)

print('#' * 52 + '  As you can see our keys are now strings!')
print('#' * 52 + '   So be careful, it is **not** true in general that `d == loads(dumps(d))`')
print('#' * 52 + '  Lets just see a few more examples that use the various JSON data types.')

d_json = '''
{
    "name": "John Cleese",
    "age": 82,
    "height": 1.96,
    "walksFunny": true,
    "sketches": [
        {
        "title": "Dead Parrot",
        "costars": ["Michael Palin"]
        },
        {
        "title": "Ministry of Silly Walks",
        "costars": ["Michael Palin", "Terry Jones"]
        }
    ],
    "boring": null    
}
'''

d = json.loads(d_json)
print(d)

from pprint import pprint
d
print()
pprint(d)
print('#' * 52 + '  The order of the keys *appears* preserved - but JSON objects are an **unordered** collection,'
                 '  so there is no guarantee of this - do not rely on it.')

print(d['age'], type(d['age']))
print(d['height'], type(d['height']))
print(d['boring'], type(d['boring']))
print(d['sketches'], type(d['sketches']))
print(d['walksFunny'], type(d['walksFunny']))
print(d['sketches'][0], type(d['sketches'][0]))

print('#' * 52 + '  As you can see the JSON `array` was serialized into a `list`,')
print('#' * 52 + '  `true` was serialized into a `bool`,')
print('#' * 52 + '   integer looking values into `int`,')
print('#' * 52 + '  float looking values into `float` and sub-objects into `dict`.')
print('#' * 52 + '  As you can see deserializing JSON objects into Python is very straightforward and intuitive')
print()
print()

print('#' * 52 + '  Lets look at tuples, and see serializing those work:')
d = {'a': (1, 2, 3)}
print(json.dumps(d))

print('#' * 52 + '  So Python tuples are serialized into JSON lists - which again means'
                 '  that if we deserialize the JSON we will not get our exact object back:')

print(json.loads(json.dumps(d)))

print('#' * 52 + '  Of course, JSON does not have a notion of tuples as a data type, so this will not work:')

bad_json = '''
    {"a": (1, 2, 3)}
'''

# json.loads(bad_json)  # JSONDecodeError: Expecting value: line 2 column 11 (char 11)

print('#' * 52 + '  Python was able to serialize a tuple by making it into a JSON array - '
                 '  but what about other data types - like Decimals, Fractions, Complex Numbers, Sets, etc?')

from decimal import Decimal
# json.dumps({'a': Decimal('0.5')})  # TypeError: Object of type 'Decimal' is not JSON serializable

print('#' * 52 + '  !!! So `Decimal` objects are not serializable. Lets see the others as well:')

try:
    json.dumps({"a": 1+1j})
except TypeError as ex:
    print(ex)

try:
    json.dumps({"a": {1, 2, 3}})
except TypeError as ex:
    print(ex)

print('#' * 52 + '  Now we could get around that problem by looking at the string representation of those objects:')

print(str(Decimal(0.5)))

print(json.dumps({"a": str(Decimal(0.5))}))

print('#' * 52 + '  But as you can see from the JSON, when we read that data back, '
                 '  we will get the **string** `0.5` back, not even a float!')
print('#' * 52 + '  How about our own objects?')
print('#' * 52 + '   As long as they have a string representation we should be fine, or will we?')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


p = Person('John', 82)
print(p)

# json.dumps({"john": p}) # TypeError: Object of type 'Person' is not JSON serializable

print('#' * 52 + '  One approach is to write a custom JSON serializer in our class itself,'
                 '  and use that when we serialize the object:')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return dict(name=self.name, age=self.age)


p = Person('John', 82)
print(p.toJSON())

print('#' * 52 + '  And now we can serialize it as follows:')

print(json.dumps({"john": p.toJSON()}, indent=2))

print('#' * 52 + '  In fact, often we can make our life a little easier by using the `vars` function (or the `__dict__`'
                 '  attribute) to return a dictionary of our object attributes:')

print(vars(p))
print(p.__dict__)

print('#' * 52 + '  ')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return vars(self)

print(json.dumps(dict(john=p.toJSON())))

print('#' * 52 + '  How about dealing with sets, where we do not control the class definition:')

s = {1, 2, 3}

print(json.dumps(dict(a=list({1, 2, 3}))))
