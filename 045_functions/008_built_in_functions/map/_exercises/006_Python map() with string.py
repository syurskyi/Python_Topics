# ___ to_upper_case(s):
#     return str(s).upper()
#
# ___ print_iterator(it):
#     ___ x in it:
#         print(x, end=' ')
#     print('')  # for new line
#
# # map() with string
# map_iterator = map(to_upper_case, 'abc')
# print(type(map_iterator))
# print_iterator(map_iterator)
#
# # Output:
# # <class 'map'>
# # A B C
#
# # Python map() with tuple
#
# # map() with tuple
# map_iterator = map(to_upper_case, (1, 'a', 'abc'))
# print_iterator(map_iterator)
#
# # Output:
# # 1 A ABC
#
# # Python map() with list
#
#
# map_iterator = map(to_upper_case, ['x', 'a', 'abc'])
# print_iterator(map_iterator)
#
# # X A ABC
#
# # Converting map to list, tuple, set
#
# map_iterator = map(to_upper_case, ['a', 'b', 'c'])
# my_list = list(map_iterator)
# print(my_list)
#
# map_iterator = map(to_upper_case, ['a', 'b', 'c'])
# my_set = set(map_iterator)
# print(my_set)
#
# map_iterator = map(to_upper_case, ['a', 'b', 'c'])
# my_tuple = tuple(map_iterator)
# print(my_tuple)
#
# # Output:
# # ['A', 'B', 'C']
# # {'C', 'B', 'A'}
# # ('A', 'B', 'C')
#
# # Python map() with lambda
#
# list_numbers = [1, 2, 3, 4]
#
# map_iterator = map(lambda x: x * 2, list_numbers)
# print_iterator(map_iterator)
#
# # Output:
# # 2 4 6 8
#
# # map() with multiple iterable arguments
# list_numbers _ 1 2 3 4
# tuple_numbers _ 5 6 7 8
# map_iterator _ m00 l.... x y x * y l..._n... t.._n...
# print_iterator m..._i...
#
# # Output: 5 12 21 32
#
# # map() with multiple iterable arguments of different sizes
# list_numbers _ 1 2 3 4
# tuple_numbers _ 5 6 7 8 9 10
# map_iterator _ m.. l.... x y x * y l...._n... t..._n...
# print_iterator m..
#
# map_iterator _ m.. l..... x y x * y t... l....
# print_iterator(map_iterator)
#
# # Output:
# # 5 12 21 32
# # 5 12 21 32
#
# # Python map() with function None
#
# map_iterator _ m.. N... 'abc'
# printm.._i..
# ___ x i_ m...........
#     print x
#
# # Output:
# #
# #
# # Traceback (most recent call last):
# #   File "/Users/pankaj/Documents/github/journaldev/Python-3/basic_examples/python_map_example.py", line 3, in <module>
# #     for x in map_iterator:
# # TypeError: 'NoneType' object is not callable
#
