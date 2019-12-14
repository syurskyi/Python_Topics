# Keyword Arguments
d = dict(a=100, b=200)
d
d = dict([('a', 100), ('b', 200)])
d
d = dict([('a', 100), ['b', 200]])
d
d = {'a': 100, 'b': 200, 'c': {'d': 1, 'e': 2}}
d

# We can also create dictionaries using a dictionary comprehension.
keys = ['a', 'b', 'c']
values = (1, 2, 3)

# We can then easily create a dictionary this way - the non-Pythonic way!

d = {}  # creates an empty dictionary
for k, v in zip(keys, values):
    d[k] = v
d

# But it is much simpler to use a dictionary comprehension:

d = {k: v for k, v in zip(keys, values)}

#  list comprehensions - you can have nested loops, if statements, etc.
keys = ['a', 'b', 'c', 'd']
values = (1, 2, 3, 4)

d = {k: v for k, v in zip(keys, values) if v % 2 == 0}
d

#  create a grid of 2D coordinate pairs, and calculate their distance from the origin:
x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)
grid = [(x, y)
         for x in x_coords
         for y in y_coords]
grid
import math
grid_extended = [(x, y, math.hypot(x, y)) for x, y in grid]
grid_extended

# We can now easily tweak this to make a dictionary, where the coordinate pairs are the key, and the distance the value:

grid_extended = {(x, y): math.hypot(x, y) for x, y in grid}

grid_extended

# Using fromkeys
counters = dict.fromkeys(['a', 'b', 'c'], 0)
counters

# If we do not specify a value, then None is used:
d = dict.fromkeys('abc')
d

# Dictionaries support the len function - this simply returns the number of key/value pairs in the dictionary:
d = dict(zip('abc', range(1, 4)))
d
len(d)

# Here we have a string where we want to count the number of each character that appears in the string.
# Since we know the alphabet is a-z, we could create a dictionary with these initial keys -
# but maybe the string contains characters outside of that, maybe punctuation marks, emojis, etc. So it's not really
# feasible to take that approach.

text = 'Put here some long text'
counts = dict()
for c in text:
    counts[c] = counts.get(c, 0) + 1
print(counts)

# We can refine this a bit - first we'll ignore spaces, then we'll want to consider lowercase and uppercase
# characters as the same:

counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)

# Membership Tests
d = dict(a=1, b=2, c=3)
'a' in d
'z' in d
'z' not in d

# Removing elements from a dictionary
# del()
d = dict.fromkeys('abcd', 0)
d
del d['a']
d

# Removing elements from a dictionary
# pop()
d = dict.fromkeys('abcd', 0)
d
result = d.pop('b')
result
d

result = d.pop('z') # Error

result = d.pop('z', 'Not found!')
result

# Removing elements from a dictionary
# popitem()
# simply removes an element from the dictionary unless the dictionary is empty, in which case it will result in
# a KeyError. The method returns a tuple containing the key and the value that was just removed.
#
d = {'a': 10, 'b': 20, 'c': 30}
d.popitem()
d.popitem()
d.popitem()

# Inserting keys with a default
# Sometimes we may want to insert an element in a dictionary with a default value, but only if the element is not
# already present:
d = {'a': 1, 'b': 2, 'c': 3}
if 'z' not in d:
    d['z'] = 0
d

# Function

def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else:
        return d[key]

print(d)

result = insert_if_not_present(d, 'a', 0)
print(result, d)

print(d)

result = insert_if_not_present(d, 'y', 10)
print(result, d)

#  setdefault()
d = {'a': 1, 'b': 2, 'c': 3}
result = d.setdefault('a', 0)
print(result)
print(d)

result = d.setdefault('z', 100)
print(result)
print(d)

# Clearing All Items
d = {'a': 1, 'b': 2, 'c': 3}
d
d.clear()
d


