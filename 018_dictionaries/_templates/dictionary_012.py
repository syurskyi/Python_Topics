# # -*- coding: utf-8 -*-
#
# # Dictionary Views
# # Union
# # Intersections
# # Differences
# # Views are special objects that support set behavior and also support iteration over the ke..,
# # values, and key/value pairs (items) i_ a dictionary.
# s1 _  1 2 3
# s2 _  2 3 4
#
# s1 | s2
# s1 & s2
# s1 - s2
#
# # We can iterate over the ke.. of a dictionary using the dictionary's iterator directly, or via the ke.. view:
# d1 _ 'a' 1 'b' 2 'c' 3
# d2 _ 'c' 30 'd' 4 'e' 5
#
# ___ key i_ d1:
#     print ke.
#
# ___ key i_ d1.ke..
#     print ke.
#
# # We can iterate over just the values of the dictionary:
# # and over the items, as tuples, of the dictionary:
# # We can also unpack the tuples directly while iterating:
# # These views are iterables, not just iterators:
# d1 _ {'a' 1 'b' 2 'c' 3
# d2 _ {'c' 30 'd' 4 'e' 5
#
# ___ value i_ d1.va..
#     print v..
#
# ___ item i_ d1.it..
#     printit..
#
# ___ k v i_ d1.it..
#     print k v
#
# ke.. _ d1.ke..
# li.. ke..
#
# # Let's say we have two dictionaries, and we want to create a new dictionary that contains all the items whose ke.. are
# # i_ both dictionaries. We want the value i_ the new dictionary to be a tuple containing all the values from both
# # dictionaries:
# d1 _ {'a' 1 'b' 2 'c' 3
# d2 _ {'b' 2 'c' 30 'd' 4
# k1 _ d1.ke..
# k2 _ d2.ke..
# k1 & k2
#
# # So we have now identified the common ke.., all that's left to do is build a dictionary from those ke.. and
# # the corresponding values.
#
# new_dict _ {}
# ___ key i_ d1.ke.. & d2.ke..
#     n._d..|key _ d1 key| d2 key|
# print n._d..
#
# # But, a dictionary comprehension would be a better approach here:
#
# new_dict _ |key d1 key| d2 key|| ___ key i_ d1.ke.. & d2.ke..
# print n.._d..
#
# # Let's tweak this a bit and generate a new dictionary, again containing just the common ke.., but whose value
# # is either the common value, or if the underlying dictionaries have different values ___ the same key,
# # choose the values from the second dictionary, discarding the values from the first.
# d1 _ 'a' 1 'b' 2 'c' 3
# d2 _ 'b' 2 'c' 30 'd' 4
# new_dict _ |key d2 key| ___ key i_ d1.ke.. & d2.ke..
# print n.._d..
#
# # suppose we have two dictionaries, and we want to identify items whose ke.. are not common to both dictionaries
# d1 _ 'a' 1 'b' 2 'c' 3 'd' 4
# d2 _ 'a' 10 'b' 20 'c' 30 'e' 5
# union _ d1.ke.. | d2.ke..
# intersection _ d1.ke.. & d2.ke..
# ke.. _ u... - i....
#
# result _ {}
# ___ key i_ ke..:
#     r.. key| _ d1.ge. key o_ d2.ge. ke.
# print r..
#
# # Or, better yet, we could use a dictionary comprehension:
#
# result _ |key d1.ge. k.. o. d2.ge. key ___ ke. i_ ke..|
# print r...
#
