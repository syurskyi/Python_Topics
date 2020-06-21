# # -*- coding: utf-8 -*-
#
# # Keyword Arguments
# d _ di__ a_100 b_200
# d
# d _ di__ | 'a' 100   'b' 200 |
# d
# d _ di__ | 'a' 100  |'b', 200|
# d
# d _ |'a' 100 'b' 200 'c' |'d' 1, 'e' 2}}
# d
#
# # We can also create dictionaries using a dictionary comprehension.
# keys _ |'a' 'b' 'c'|
# values _  1 2 3
#
# # We can then easily create a dictionary this way - the non-Pythonic way!
#
# d _ ||  # creates an empty dictionary
# ___ k, v i_ zi. k.. v...
#     d|k| _ v
# d
#
# # But it is much simpler to use a dictionary comprehension:
#
# d _ |k: v ___ k, v i_ zi. k.. v.. |
#
# #  list comprehensions - you can have nested loops, i_ statements, etc.
# keys _ |'a' 'b' 'c' 'd'|
# values _  1 2 3 4
#
# d _ |k v ___ k v i_ zi. k.. v...  i_ v % 2 __ 0|
# d
#
# #  create a grid of 2D coordinate pairs, and calculate their distance from the origin:
# x_coords _  -2, -1, 0, 1, 2
# y_coords _  -2, -1, 0, 1, 2
# grid _ | x, y
#          ___ x i_ x_coords
#          ___ y i_ y_coords|
# grid
# ______ math
# grid_extended _ | x, y, ma__.hy___ x y ___ x, y i_ grid|
# grid_extended
#
# # We can now easily tweak this to make a dictionary, where the coordinate pairs are the key, and the distance the value:
#
# grid_extended _ | x, y  ma__.hy__ x y  ___ x, y i_ grid|
#
# grid_extended
#
# # Using fromkeys
# counters _ di__.f___ |'a', 'b', 'c'|, 0
# counters
#
# # i_ we do not specify a value, then None is used:
# d _ di__.fromkeys 'abc'
# d
#
# # Dictionaries support the len function - this simply returns the number of key/value pairs i_ the dictionary:
# d _ di__ zi. 'abc' ra... 1, 4
# d
# le. d
#
# # Here we have a string where we want to count the number of each character that appears i_ the string.
# # Since we know the alphabet is a-z, we could create a dictionary with these initial keys -
# # but maybe the string contains characters outside of that, maybe punctuation marks, emojis, etc. So it's not really
# # feasible to take that approach.
#
# text _ 'Put here some long text'
# counts _ di__
# ___ c i_ text:
#     co...|c| _ co___.ge. c, 0  + 1
# print counts
#
# # We can refine this a bit - first we'll ignore spaces, then we'll want to consider lowercase and uppercase
# # characters as the same:
#
# counts _ di__
# ___ c i_ text
#     key _ c.lo..  .str..
#     i_ key:
#         co...|key| _ co___.ge. ke., 0  + 1
# print counts
#
# # Membership Tests
# d _ di__ a_1, b_2, c_3
# 'a' i_ d
# 'z' i_ d
# 'z' no. i_ d
#
# # Removing elements from a dictionary
# # del
# d _ di__.fr... 'abcd', 0
# d
# de. d|'a'|
# d
#
# # Removing elements from a dictionary
# # pop
# d _ di__.fr... 'abcd', 0
# d
# result _ d.po. 'b'
# result
# d
#
# result _ d.po. 'z'  # Error
#
# result _ d.po. 'z', 'Not found!'
# result
#
# # Removing elements from a dictionary
# # popitem
# # simply removes an element from the dictionary unless the dictionary is empty, i_ which case it will result i_
# # a KeyError. The method returns a tuple containing the key and the value that was just removed.
# #
# d _ |'a' 10, 'b' 20, 'c' 30|
# d.p_i_
# d.p_i_
# d.p_i_
#
# # Inserting keys with a default
# # Sometimes we may want to insert an element i_ a dictionary with a default value, but only i_ the element is not
# # already present:
# d _ |'a' 1 'b' 2, 'c' 3|
# i_ 'z' no. i_ d
#     d|'z'| _ 0
# d
#
# # Function
#
# ___ insert_if_not_present d, key, value :
#     i_ ke. no. i_ d:
#         d|ke.| _ value
#         r_ v...
#     else:
#         r_ d|ke.|
#
# print d
#
# result _ insert_if_not_present d, 'a', 0
# print r.... d
#
# print d
#
# result _ insert_if_not_present d, 'y', 10
# print r...., d
#
# #  setdefault
# d _ |'a' 1 'b' 2 'c' 3|
# result _ d.s_d_ 'a', 0
# print r...
# print d
#
# result _ d.s_d_ 'z', 100
# print r...
# print d
#
# # Clearing All Items
# d _ |'a' 1 'b' 2 'c' 3|
# d
# d.c___
# d
#
#
