from collections import OrderedDict

# Equality Comparisons
# With regular dictionaries, two dictionaries are considered equal (==) if they contain the same key/value pairs, irrespective of the ordering.

d1 = {'a': 10, 'b': 20}
d2 = {'b': 20, 'a': 10}

d1 == d2
# True

# But this is not the case with OrderedDicts - since ordering matters here, two OrderedDicts will compare equal if both their key/values pairs are equal and if the keys are in the same order:

d1 = OrderedDict()
d1['a'] = 10
d1['b'] = 20
d2 = OrderedDict()
d2['a'] = 10
d2['b'] = 20
d3 = OrderedDict()
d3['b'] = 20
d3['a'] = 10
print(d1)
print(d2)
print(d3)
# OrderedDict([('a', 10), ('b', 20)])
# OrderedDict([('a', 10), ('b', 20)])
# OrderedDict([('b', 20), ('a', 10)])

d1 == d2
# True

d1 == d3
# False

# Now, an OrderedDict is a subclass of a standard dict:

isinstance(d1, OrderedDict)
# True

isinstance(d1, dict)
# True

# So, can we compare an OrderedDict with a plain dict?
# The answer is yes, and in this case order does not matter:

d1 = OrderedDict()
d1['a'] = 10
d1['b'] = 20
d2 = {'b': 20, 'a': 10}
print(d1)
print(d2)
# OrderedDict([('a', 10), ('b', 20)])
# {'b': 20, 'a': 10}

d1 == d2
# True

d2 == d1
# True