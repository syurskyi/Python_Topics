# # OrderedDict¶
# #
# # An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
#
# ____ c..
#
# print('Regular dictionary:')
# d _
# . 'a' _ 'A'
# . 'b' _ 'B'
# . 'c' _ 'C'
# . 'd' _ 'D'
# . 'e' _ 'E'
#
# ___ k v i_ d.it..
#     print k v
#
# print('\nOrderedDict:')
# d _ c___.O..
# . 'a' _ 'A'
# . 'b' _ 'B'
# . 'c' _ 'C'
# . 'd' _ 'D'
# . 'e' _ 'E'
#
# ___ k, v i_ d.it..
#     print k v
#
# # A regular dict does not track the insertion order, and iterating over it produces the values in an arbitrary order.
# # In an OrderedDict, by contrast, the order the items are inserted is remembered and used when creating an iterator
#
# # $ python collections_ordereddict_iter.py
# #
# # Regular dictionary:
# # a A
# # c C
# # b B
# # e E
# # d D
# #
# # OrderedDict:
# # a A
# # b B
# # c C
# # d D
# # e E
#
# # Equality
# #
# # A regular dict looks at its contents when testing for equality. An OrderedDict also considers
# # the order the items were added.
#
# ____ c..
#
# print('dict       :',)
# d1 _
# .. 'a' _ 'A'
# .. 'b' _ 'B'
# .. 'c' _ 'C'
# .. 'd' _ 'D'
# .. 'e' _ 'E'
#
# d2 _
# .. 'e' _ 'E'
# .. 'd' _ 'D'
# .. 'c' _ 'C'
# .. 'b' _ 'B'
# .. 'a' _ 'A'
#
# print(d1 _ d2)
#
# print('OrderedDict:',)
#
# d1 _ c__.O..
# .. 'a' _ 'A'
# .. 'b' _ 'B'
# .. 'c' _ 'C'
# .. 'd' _ 'D'
# .. 'e' _ 'E'
#
# d2 _ c__.O..
# ..'e' _ 'E'
# ..'d' _ 'D'
# ..'c' _ 'C'
# ..'b' _ 'B'
# ..'a' _ 'A'
#
# print(d1 __ d2)
#
# # In this case, since the two ordered dictionaries are created from values in a different order,
# # they are considered to be different.
# #
# # $ python collections_ordereddict_equality.py
# #
# # dict       : True
# # OrderedDict: False