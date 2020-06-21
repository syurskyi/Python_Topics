# # Counter
# # A Counter is a container that keeps track of how many times equivalent values are added.
# # It can be used to implement the same algorithms for which bag or multiset data structures are commonly used in
# # other languages.
# # Initializing
# # Counter supports three forms of initialization. Its constructor can be called with a sequence of items,
# # a dictionary containing keys and counts, or using keyword arguments mapping string names to counts.
#
# _______ c..
#
# print c...C.. 'a', 'b', 'c', 'a', 'b', 'b'
# print c...C.. 'a' 2, 'b' 3, 'c' 1
# print(c...C..(a_2, b_3, c_1
#
# # The results of all three forms of initialization are the same.
#
# # $ python collections_counter_init.py
# # Counter({'b': 3, 'a': 2, 'c': 1})
# # Counter({'b': 3, 'a': 2, 'c': 1})
# # Counter({'b': 3, 'a': 2, 'c': 1})
#
# # An empty Counter can be constructed with no arguments and populated via the update() method.
#
# _______ c..
#
# c = c...C..
# print 'Initial :' c
# c.up.. 'abcdaab'
# print('Sequence:'  c
# c.up.. 'a' 1 'd' 5
# print 'Dict    :' c
#
# # The count values are increased based on the new data, rather than replaced. In this example, the count for a goes
# # from 3 to 4.
# #
# # $ python collections_counter_update.py
# #
# # Initial : Counter()
# # Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
# # Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})
# #
# # Accessing Counts
# # Once a Counter is populated, its values can be retrieved using the dictionary API.
#
# _______ c..
#
# c = c...C.. 'abcdaab'
# ___ letter i_ 'abcde':
#     print */ : /' / le..; c |le..
#
# # Counter does not raise KeyError for unknown items. If a value has not been seen in the input
# # (as with e in this example), its count is 0.
#
# # $ python collections_counter_get_values.py
# #
# # a : 3
# # b : 2
# # c : 1
# # d : 1
# # e : 0
#
# # The elements() method returns an iterator that produces all of the items known to the Counter.
#
# _______ c..
#
# c = c...C.. 'extremely'
# c 'z' _ 0
# print(c)
# print li.. c.el..
#
# # The order of elements is not guaranteed, and items with counts less than zero are not included.
# #
# # $ python collections_counter_elements.py
# #
# # Counter({'e': 3, 'm': 1, 'l': 1, 'r': 1, 't': 1, 'y': 1, 'x': 1, 'z': 0})
# # ['e', 'e', 'e', 'm', 'l', 'r', 't', 'y', 'x']
# #
# # Use most_common() to produce a sequence of the n most frequently encountered input values and their respective counts.
#
# _______ c..
#
# c = c...C..()
# w___ op.. '/usr/share/dict/words' '__') a. f
#     ___ line i_ f
#         c.up.. li__.rst__.lo..
#
# print('Most common:')
# ___ letter count i_ c.m.._c.. 3
#     print */: /7_' /  le... co...
#
# # This example counts the letters appearing in all of the words in the system dictionary to produce a frequency
# # distribution, then prints the three most common letters. Leaving out the argument to most_common() produces a list
# # of all the items, in order of frequency.
# #
# # $ python collections_counter_most_common.py
# #
# # Most common:
# # e:  235331
# # i:  201032
# # a:  199554
# #
# # Arithmetic
# #
# # Counter instances support arithmetic and set operations for aggregating results.
#
# _______ c..
#
# c1 _ c...C.. 'a', 'b', 'c', 'a', 'b', 'b'
# c2 _ c...C..'alphabet'
#
# print('C1:', c1)
# print('C2:', c2)
# print('\nCombined counts:')
# print(c1 + c2)
# print('\nSubtraction:')
# print(c1 - c2)
# print('\nIntersection (taking positive minimums):')
# print(c1 & c2)
# print('\nUnion (taking maximums):')
# print(c1 | c2)
#
# # Each time a new Counter is produced through an operation, any items with zero or negative counts are discarded.
# # The count for a is the same in c1 and c2, so subtraction leaves it at zero.
# #
# # $ python collections_counter_arithmetic.py
# #
# # C1: Counter({'b': 3, 'a': 2, 'c': 1})
# # C2: Counter({'a': 2, 'b': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})
# #
# # Combined counts:
# # Counter({'a': 4, 'b': 4, 'c': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})
# #
# # Subtraction:
# # Counter({'b': 2, 'c': 1})
# #
# # Intersection (taking positive minimums):
# # Counter({'a': 2, 'b': 1})
# #
# # Union (taking maximums):
# # Counter({'b': 3, 'a': 2, 'c': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})
#
