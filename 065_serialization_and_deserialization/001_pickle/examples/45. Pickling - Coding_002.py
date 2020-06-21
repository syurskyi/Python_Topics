# n this part of the course I am only going to discuss pickling basic data types such as numbers, strings, tuples,
# lists, sets and dictionaries.
# In general tuples, lists, sets and dictionaries are all picklable as long as their elements are themselves picklable.
# Let's start by serializing some simple data types, such as strings and numbers.
# Instead of serializing to a file, I will store the resulting pickle data in a variable, so we can easily
# inspect it and unpickle it:

import pickle

ser = pickle.dumps('Python Pickled Peppers')

print(ser)
# b'\x80\x03X\x16\x00\x00\x00Python Pickled Peppersq\x00.'
# ######################################################################################################################

print('#' * 52 + ' We can deserialize the data this way:  ')

deser = pickle.loads(ser)
print(deser)
# 'Python Pickled Peppers'
# ######################################################################################################################

print('#' * 52 + ' We can do the same thing with numerics ')
ser = pickle.dumps(3.14)
print(ser)
deser = pickle.loads(ser)
print(deser)
# 3.14
# ######################################################################################################################

print('#' * 52 + ' We can do the same with lists and tuples:  ')
d = [10, 20, ('a', 'b', 30)]
ser = pickle.dumps(d)
print(ser)
# b'\x80\x03]q\x00(K\nK\x14X\x01\x00\x00\x00aq\x01X\x01\x00\x00\x00bq\x02K\x1e\x87q\x03e.'
# ######################################################################################################################

deser = pickle.loads(ser)
print(deser)
# [10, 20, ('a', 'b', 30)]
# ######################################################################################################################

print('#' * 52 + '  Note that the original and the deserialized objects are equal, but not identical:')
print(d is deser, d == deser)
# (False, True)
# ######################################################################################################################

print('#' * 52 + '  This works the same way with sets too:')
s = {'a', 'b', 'x', 10}
print(s)
# {10, 'a', 'b', 'x'}
# ######################################################################################################################

ser = pickle.dumps(s)
print(ser)
# b'\x80\x03cbuiltins\nset\nq\x00]q\x01(X\x01\x00\x00\x00aq\x02K\nX\x01\x00\x00\x00xq\x03X\x01\x00\x00\x00bq\x04e\x85q\x05Rq\x06.'
# ######################################################################################################################

deser = pickle.loads(ser)
print(deser)
# {'a', 10, 'b', 'x'}
# ######################################################################################################################

print('#' * 52 + '  And finally, we can pickle dictionaries as well:')
d = {'b': 1, 'a': 2, 'c': {'x': 10, 'y': 20}}
print(d)
# {'b': 1, 'a': 2, 'c': {'x': 10, 'y': 20}}
# ######################################################################################################################

ser = pickle.dumps(d)
print(ser)
# b'\x80\x03}q\x00(X\x01\x00\x00\x00bq\x01K\x01X\x01\x00\x00\x00aq\x02K\x02X\x01\x00\x00\x00cq\x03}q\x04(X\x01\x00\x00\x00xq\x05K\nX\x01\x00\x00\x00yq\x06K\x14uu.'
# ######################################################################################################################

deser = pickle.loads(ser)
print(deser)
# {'b': 1, 'a': 2, 'c': {'x': 10, 'y': 20}}
# ######################################################################################################################

print(d == deser)
# True

print('#' * 52 + '  What happens if we pickle a dictionary that has two of its values set to another dictionary?')
d1 = {'a': 10, 'b': 20}
d2 = {'x': 100, 'y': d1, 'z': d1}
print(d2)
# {'x': 100, 'y': {'a': 10, 'b': 20}, 'z': {'a': 10, 'b': 20}}
# ######################################################################################################################

ser = pickle.dumps(d2)
d3 = pickle.loads(ser)
print(d3)
# {'x': 100, 'y': {'a': 10, 'b': 20}, 'z': {'a': 10, 'b': 20}}
# ######################################################################################################################

print('#' * 52 + '  That seems to work... Is that sub-dictionary still the same as the original one?')
print(d3['y'] == d2['y'])
# True
# ######################################################################################################################

print(d3['y'] is d2['y'])
# False
# ######################################################################################################################

print('#' * 52 + '  But consider the original dictionary d2: both the x and y keys referenced the same dictionary d1:')
print(d2['y'] is d2['z'])
# True
# ######################################################################################################################

print('#' * 52 + '  How did this work with our deserialized dictionary?')
print(d3['y'] == d3['z'])
# True
# ######################################################################################################################

# As you can see the relative shared object is maintained.
# As you can see our dictionary d looks like the earlier one. So, when Python serializes the dictionary,
# it behaves very similarly to serializing a deep copy of the dictionary. The same thing happens with other collections
# types such as lists, sets, and tuples.
# What this means though is that you have to be very careful how you use serialization and deserialization.
# Consider this piece of code:

print('#' * 52 + '  As you can see the relative shared object is maintained.')
print('#' * 52 + '  ')

print('#' * 52 + '  What this means though is that you have to be very careful how you use serialization and '
                 'deserialization.')
d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': d1}
print(d1)
print(d2)
d1['c'] = 3
print(d1)
print(d2)
# {'a': 1, 'b': 2}
# {'x': 10, 'y': {'a': 1, 'b': 2}}
# {'a': 1, 'b': 2, 'c': 3}
# {'x': 10, 'y': {'a': 1, 'b': 2, 'c': 3}}
# ######################################################################################################################

print('#' * 52 + '  Now suppose we pickle our dictionaries to restore those values the next time around, '
                 '  but use the same code, expecting the same result:')

d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': d1}
d1_ser = pickle.dumps(d1)
d2_ser = pickle.dumps(d2)

# simulate exiting the program, or maybe just restarting the notebook
del d1
del d2

# load the data back up
d1 = pickle.loads(d1_ser)
d2 = pickle.loads(d2_ser)

# and continue processing as before
print(d1)
print(d2)
d1['c'] = 3
print(d1)
print(d2)
# {'a': 1, 'b': 2}
# {'x': 10, 'y': {'a': 1, 'b': 2}}
# {'a': 1, 'b': 2, 'c': 3}
# {'x': 10, 'y': {'a': 1, 'b': 2}}
# ######################################################################################################################

# So just remember that as soon as you pickle a dictionary, whatever object references it had to another object is
# essentially lost - just as if you had done a deep copy first. It's a subtle point, but one that can easily lead
# to bugs if we're not careful.
# However, the pickle module is relatively intelligent and will not re-pickle an object it has already pickled -
# which means that relative references are preserved.
# Let's see an example of what I mean by this:

print('#' * 52 + '  So just remember that as soon as you pickle a dictionary, '
                 '  whatever object references it had to another object is essentially lost - '
                 '  just as if you had done a deep copy first. '
                 '  It is a subtle point, but one that can easily lead to bugs if we are not careful.')
print('#' * 52 + '  ')
print('#' * 52 + '  However, the pickle module is relatively intelligent and will not re-pickle an object it has'
                 '  already pickled - which means that relative references are preserved.')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


john = Person('John Cleese', 79)
eric = Person('Eric Idle', 75)
michael = Person('Michael Palin', 75)

parrot_sketch = {
    "title": "Parrot Sketch",
    "actors": [john, michael]
}

ministry_sketch = {
    "title": "Ministry of Silly Walks",
    "actors": [john, michael]
}

joke_sketch = {
    "title": "Funniest Joke in the World",
    "actors": [eric, michael]
}

fan_favorites = {
    "user_1": [parrot_sketch, joke_sketch],
    "user_2": [parrot_sketch, ministry_sketch]
}


from pprint import pprint
pprint(fan_favorites)
# {'user_1': [{'actors': [Person(name=John Cleese, age=79),
#                         Person(name=Michael Palin, age=75)],
#              'title': 'Parrot Sketch'},
#             {'actors': [Person(name=Eric Idle, age=75),
#                         Person(name=Michael Palin, age=75)],
#              'title': 'Funniest Joke in the World'}],
#  'user_2': [{'actors': [Person(name=John Cleese, age=79),
#                         Person(name=Michael Palin, age=75)],
#              'title': 'Parrot Sketch'},
#             {'actors': [Person(name=John Cleese, age=79),
#                         Person(name=Michael Palin, age=75)],
#              'title': 'Ministry of Silly Walks'}]}
# ######################################################################################################################

print('#' * 52 + '  As you can see we have some shared references, for example:')
print(fan_favorites['user_1'][0] is fan_favorites['user_2'][0])
# True
# ######################################################################################################################

print('#' * 52 + '  Lets store the id of the parrot_sketch for later reference:')
parrot_id_original = id(parrot_sketch)

print('#' * 52 + '  Now lets pickle and unpickle this object:')
ser = pickle.dumps(fan_favorites)
new_fan_favorites = pickle.loads(ser)
print(fan_favorites == new_fan_favorites)
# True
# ######################################################################################################################

print('#' * 52 + '  And lets look at the id of the parrot_sketch object in our new dictionary'
                 '  compared to the original one:')
print(id(fan_favorites['user_1'][0]), id(new_fan_favorites['user_1'][0]))
# (4554999848, 4555001288)
# ######################################################################################################################

print('#' * 52 + '  As expected the ids differ - but the objects are equal:')
print(fan_favorites['user_1'][0] == new_fan_favorites['user_1'][0])
# True
# ######################################################################################################################

print('#' * 52 + '  But now lets look at the parrot sketch that is in both user_1 and user_2 - '
                 '  remember that originally the objects were identical (is):')
print(fan_favorites['user_1'][0] is fan_favorites['user_2'][0])
# True
# ######################################################################################################################

print('#' * 52 + '  and with our new object:')
print(new_fan_favorites['user_1'][0] is new_fan_favorites['user_2'][0])
# True
# ######################################################################################################################

print('#' * 52 + '  As you can see the relative relationship between objects that were pickled is preserved.')

# And that's all I'm really going to say about pickling objects in Python. Instead I'm going to focus more on what
# is probably a more relevant topic to many of you - JSON serialization/deserialization.
