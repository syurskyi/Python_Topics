# JSON Serialization
# As we saw in the lecture, JSON is an extremely popular format for data interchange. Unlike pickling it is safe,
# because JSON data is basically just text. It's human readable too, which is a plus.
# There are other formats too, such as XML - but XML does not translate directly to Python dictionaries like JSON does.
# JSON is a far more natural fit with Python - in fact, when we view the contents of a Python dictionary it reminds us
# of JSON.

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

# This is a standard Python dictionary, but if you look at the format, it is also technically JSON.
# A JSON object contains key/value pairs, nested objects and arrays - just like a Python dictionary.
# The big difference is that JSON is basically just one big string, while a Python dictionary is an object containing
# other objects.
# So the big question when we want to "convert" (serialize) a Python object to JSON is how to represent Python objects
# as strings.
# Conversely, if we want to load a JSON object into a Python dictionary, how do we "convert" (deserialize)
# the JSON value strings into a Python object.
# By the way this concept of serializing/deserializing is also often called marshalling.
# JSON has just a few data types it supports:
# Strings: must be delimited by double quotes
# Booleans: the values true and false
# Numbers: can be integers, or floats (including exponential notation, 1.3E2 for example), but are all considered floats
# in the standard
# Arrays: an ordered collection of zero or more items of any valid JSON type
# Objects: an unordered collection of key:value pairs - the keys must be strings (so delimited by double quotes),
# and the values can be any valid JSON type.
# NULL: a null object, denoted by null and equivalent to None in Python.
# This means that the data types supported by JSON are relatively limited - but it turns out, as we'll see later,
# that it's not really a limitation.
#
# Any object can be serialized into a string (think of the __repr__ method we've used often throughout this course) -
# in fact, any piece of information in your computer is a series of bits, as are characters - so theoretically
# any piece of information can be represented using characters. We'll come back to this in a later video. For now,
# we're going to stick with the basic data types supported by JSON and see what Python provides us for marshalling JSON.
#
# We are going to use the json module:


import json

# In Python, serializing a dictionary to JSON is done using the dump and dumps functions - they are just variants
# of the same thing - dumps serializes to a string, while dump writes the serialization to a file
# (or more accurately, a stream).
# Similarly, the load and loads functions are used to deserialize JSON into a dictionary.
# Let's see a quick example first:

d1 = {"a": 100, "b": 200}
d1_json = json.dumps(d1)
print(d1_json, type(d1_json))
# ('{"a": 100, "b": 200}', str)
# ######################################################################################################################

print('#' * 52 + '  By the way, we can obtain a better looking JSON string by specifying'
                 '  an indent for the `dump` or `dumps` functions:')

print(json.dumps(d1, indent=2))
#
# {
#   "a": 100,
#   "b": 200
# }
# ######################################################################################################################
# And we can deserialize the JSON string:

print('#' * 52 + '  And we can deserialize the JSON string:')

d2 = json.loads(d1_json)

print(d2, type(d2))
print(d1 == d2)
# ({'a': 100, 'b': 200}, dict)
# True
# ######################################################################################################################

# In fact, the original dictionary and the new one are equal.

print('#' * 52 + '  There is a big caveat here.')
print('#' * 52 + '   In Python, keys can be any hashable object.')
print('#' * 52 + '  But remember that in JSON keys must be strings!')

d1 = {1: 100, 2: 200}
d1_json = json.dumps(d1)
print(d1_json)
# '{"1": 100, "2": 200}'
# ######################################################################################################################

print('#' * 52 + '  Notice how the keys are now strings in the JSON "object".')
print('#' * 52 + '  And when we deserialize:')

d2 = json.loads(d1_json)

print(d1)
print(d2)
# {1: 100, 2: 200}
# {'1': 100, '2': 200}
# ######################################################################################################################

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
# {'name': 'John Cleese', 'age': 82, 'height': 1.96, 'walksFunny': True, 'sketches': [{'title': 'Dead Parrot', 'costars': ['Michael Palin']}, {'title': 'Ministry of Silly Walks', 'costars': ['Michael Palin', 'Terry Jones']}], 'boring': None}
# ######################################################################################################################

from pprint import pprint
d
print()
pprint(d)
# ######################################################################################################################

# Important: The order of the keys appears preserved - but JSON objects are an unordered collection, so there is
# no guarantee of this - do not rely on it.
# Let's see the various data types in our dictionary:

print('#' * 52 + '  The order of the keys *appears* preserved - but JSON objects are an **unordered** collection,'
                 '  so there is no guarantee of this - do not rely on it.')

print(d['age'], type(d['age']))
print(d['height'], type(d['height']))
print(d['boring'], type(d['boring']))
print(d['sketches'], type(d['sketches']))
print(d['walksFunny'], type(d['walksFunny']))
print(d['sketches'][0], type(d['sketches'][0]))
# 82 <class 'int'>
# 1.96 <class 'float'>
# None <class 'NoneType'>
# [{'title': 'Dead Parrot', 'costars': ['Michael Palin']}, {'title': 'Ministry of Silly Walks', 'costars': ['Michael Palin', 'Terry Jones']}] <class 'list'>
# True <class 'bool'>
# {'title': 'Dead Parrot', 'costars': ['Michael Palin']} <class 'dict'>
# ######################################################################################################################

# As you can see the JSON array was serialized into a list, true was serialized into a bool, integer looking values
# into int, float looking values into float and sub-objects into dict. As you can see deserializing JSON objects into
# Python is very straightforward and intuitive.
# Let's look at tuples, and see serializing those work:

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
# '{"a": [1, 2, 3]}'
# ######################################################################################################################

print('#' * 52 + '  So Python tuples are serialized into JSON lists - which again means'
                 '  that if we deserialize the JSON we will not get our exact object back:')

print(json.loads(json.dumps(d)))
# {'a': [1, 2, 3]}
# ######################################################################################################################

print('#' * 52 + '  Of course, JSON does not have a notion of tuples as a data type, so this will not work:')

bad_json = '''
    {"a": (1, 2, 3)}
'''

# json.loads(bad_json)  # JSONDecodeError: Expecting value: line 2 column 11 (char 11)

# We get a JSONDecodeError exception. And that's an exception you'll run across quite a bit as you work with JSON
# data and Python objects!
# So, Python was able to serialize a tuple by making it into a JSON array - but what about other data types -
# like Decimals, Fractions, Complex Numbers, Sets, etc?

print('#' * 52 + '  Python was able to serialize a tuple by making it into a JSON array - '
                 '  but what about other data types - like Decimals, Fractions, Complex Numbers, Sets, etc?')

from decimal import Decimal
# json.dumps({'a': Decimal('0.5')})  # TypeError: Object of type 'Decimal' is not JSON serializable
# TypeError: Object of type 'Decimal' is not JSON serializable
# So Decimal objects are not serializable. Let's see the others as well:

print('#' * 52 + '  !!! So `Decimal` objects are not serializable. Lets see the others as well:')

try:
    json.dumps({"a": 1+1j})
except TypeError as ex:
    print(ex)

# Object of type 'complex' is not JSON serializable

try:
    json.dumps({"a": {1, 2, 3}})
except TypeError as ex:
    print(ex)
# Object of type 'set' is not JSON serializable
# Now we could get around that problem by looking at the string representation of those objects

print('#' * 52 + '  Now we could get around that problem by looking at the string representation of those objects:')

print(str(Decimal(0.5)))
# '0.5'
# ######################################################################################################################

print(json.dumps({"a": str(Decimal(0.5))}))
# '{"a": "0.5"}'
# ######################################################################################################################

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
# TypeError: Object of type 'Person' is not JSON serializable
# So no luck there either. One approach is to write a custom JSON serializer in our class itself,
# and use that when we serialize the object:

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
# {'name': 'John', 'age': 82}
# ######################################################################################################################

print('#' * 52 + '  And now we can serialize it as follows:')

print(json.dumps({"john": p.toJSON()}, indent=2))
# {
#   "john": {
#     "name": "John",
#     "age": 82
#   }
# }
# ######################################################################################################################
# In fact, often we can make our life a little easier by using the vars function (or the __dict__ attribute)
# to return a dictionary of our object attributes:

print('#' * 52 + '  In fact, often we can make our life a little easier by using the `vars` function (or the `__dict__`'
                 '  attribute) to return a dictionary of our object attributes:')

print(vars(p))
# {'name': 'John', 'age': 82}
# ######################################################################################################################

print(p.__dict__)
# {'name': 'John', 'age': 82}
# ######################################################################################################################

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
# '{"john": {"name": "John", "age": 82}}'
# ######################################################################################################################

print('#' * 52 + '  How about dealing with sets, where we do not control the class definition:')

s = {1, 2, 3}
# We can't use the string representation (it has curly braces), and there's nothing else really handy - but we could
# just convert it to a list:

print(json.dumps(dict(a=list({1, 2, 3}))))
# '{"a": [1, 2, 3]}'
# ######################################################################################################################

# There are a couple of glaring issues at this point:
# we have to remember to call .toJSON() for our custom objects
# what about built-in or standard types like sets, or dates? use built-in or write custom functions to convert
# and call them every time?
# There has to be a better way... !

