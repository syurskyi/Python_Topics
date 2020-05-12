# ____ u__ ______ T..
#
#
# c_ TestAssertions T..
#     """
#     Showcase for different assertions provided by the unittest library.
#     These are just a few examples and do not cover every assertion method provided.
#     For the full documentation see the python docs: https://docs.python.org/3/library/unittest.html
#     """
#
#     ___ test_equality
#         x _ 42
#         y _ 42
#
#         aE.. x, y
#         aNE.. 42, 1337
#
#     ___ test_none_values
#         x _ 42
#         y _ N..
#
#         aIN.. N..
#         aIN.. y
#         aINN.. x
#
#     ___ test_bool
#         aT.. 1 __ 1
#         aF.. 1 __ 0
#
#     ___ test_comparison
#         aG.. 1337, 42
#         aGE.. 13, 13
#         aL.. 42, 1337
#         aLE.. 13, 13
#         aAE.. 2.012, 2.013, 2
#         aNAE.. 2.012, 2.013, 3
#
#     ___ test_exceptions
#         w__ aR.. Z..
#             x _ 42 / 0
#
#     ___ test_list_comparison
#         list1 _ [1, 2, 3]
#         list2 _ [1, 2, 3]
#         list3 _ [3, 2, 1]
#         aLE.. _1 _2
#         aCE.. _1, _3
#         # same methods exist for strings, sequences, tuples, sets and dictionaries
