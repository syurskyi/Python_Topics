# OrderedDict¶
#
# An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.

import collections

print('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

print('\nOrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

# A regular dict does not track the insertion order, and iterating over it produces the values in an arbitrary order.
# In an OrderedDict, by contrast, the order the items are inserted is remembered and used when creating an iterator

# $ python collections_ordereddict_iter.py
#
# Regular dictionary:
# a A
# c C
# b B
# e E
# d D
#
# OrderedDict:
# a A
# b B
# c C
# d D
# e E

# Equality
#
# A regular dict looks at its contents when testing for equality. An OrderedDict also considers
# the order the items were added.

import collections

print('dict       :',)
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = {}
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

print('OrderedDict:',)

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = collections.OrderedDict()
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

# In this case, since the two ordered dictionaries are created from values in a different order,
# they are considered to be different.
#
# $ python collections_ordereddict_equality.py
#
# dict       : True
# OrderedDict: False