# Dictionary Views
# Union
# Intersections
# Differences
# Views are special objects that support set behavior and also support iteration over the keys,
# values, and key/value pairs (items) in a dictionary.
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1 | s2
s1 & s2
s1 - s2

# We can iterate over the keys of a dictionary using the dictionary's iterator directly, or via the keys view:
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'c': 30, 'd': 4, 'e': 5}

for key in d1:
    print(key)

for key in d1.keys():
    print(key)

# We can iterate over just the values of the dictionary:
# and over the items, as tuples, of the dictionary:
# We can also unpack the tuples directly while iterating:
# These views are iterables, not just iterators:
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'c': 30, 'd': 4, 'e': 5}

for value in d1.values():
    print(value)

for item in d1.items():
    print(item)

for k, v in d1.items():
    print(k, v)

keys = d1.keys()
list(keys)

# Let's say we have two dictionaries, and we want to create a new dictionary that contains all the items whose keys are
# in both dictionaries. We want the value in the new dictionary to be a tuple containing all the values from both
# dictionaries:
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}
k1 = d1.keys()
k2 = d2.keys()
k1 & k2

# So we have now identified the common keys, all that's left to do is build a dictionary from those keys and
# the corresponding values.

new_dict = {}
for key in d1.keys() & d2.keys():
    new_dict[key] = (d1[key], d2[key])
print(new_dict)

# But, a dictionary comprehension would be a better approach here:

new_dict = {key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()}
print(new_dict)

# Let's tweak this a bit and generate a new dictionary, again containing just the common keys, but whose value
# is either the common value, or if the underlying dictionaries have different values for the same key,
# choose the values from the second dictionary, discarding the values from the first.
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}
new_dict = {key: d2[key] for key in d1.keys() & d2.keys()}
print(new_dict)

# suppose we have two dictionaries, and we want to identify items whose keys are not common to both dictionaries
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}
union = d1.keys() | d2.keys()
intersection = d1.keys() & d2.keys()
keys = union - intersection

result = {}
for key in keys:
    result[key] = d1.get(key) or d2.get(key)
print(result)

# Or, better yet, we could use a dictionary comprehension:

result = {key: d1.get(key) or d2.get(key) for key in keys}
print(result)

