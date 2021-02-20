def to_upper_case(s):
    return str(s).upper()


def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line

# map() with string
map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print(map_iterator)
print(list(map_iterator))

# Output:
# <class 'map'>
# A B C

# Python map() with tuple

# map() with tuple
map_iterator = map(to_upper_case,(1, 'a', 'abc'))
print_iterator(map_iterator)

# Output:
# 1 A ABC

# Python map() with list


map_iterator = map(to_upper_case, ['x', 'a', 'abc'])
print_iterator(map_iterator)

# X A ABC
#
# Converting map to list, tuple, set

# map_iterator = map(t.. |'a', 'b', 'c'
# my_list = li.. ?
# print ?
#
# map_iterator = m.. t... |'a', 'b', 'c'
# my_set = se. ?
# print ?
#
# map_iterator = m.. t... |'a', 'b', 'c'
# my_tuple = tu.. ?
# print ?

# # Output:
# # ['A', 'B', 'C']
# # {'C', 'B', 'A'}
# # ('A', 'B', 'C')
#
# # Python map() with lambda
#
# list_numbers = [1, 2, 3, 4]
#
# map_iterator = m.. l___ x ? * 2 ?
# p... ?
#
# # Output:
# # 2 4 6 8
#
# map() with multiple iterable arguments
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)
map_iterator = map(lambda x, y: x * y, list_numbers, tuple_numbers)
print_iterator(map_iterator)
#
# # Output: 5 12 21 32
#
# # map() with multiple iterable arguments of different sizes
# list_numbers _ 1 2 3 4
# tuple_numbers _ 5 6 7 8 9 10
# map_iterator _ m.. l____ x y x * y ?1 ?2
# p... ?
#
# map_iterator _ m.. l___ x y x * y t... l....
# p... ?
#
# # Output:
# # 5 12 21 32
# # 5 12 21 32
#
# # Python map() with function None
#
# map_iterator _ m.. N... 'abc'
# print ?
# ___ x __ ?
#     print ?
#
# # Output:
# #
# #
# # Traceback (most recent call last):
# #   File "/Users/pankaj/Documents/github/journaldev/Python-3/basic_examples/python_map_example.py", line 3, in <module>
# #     for x in map_iterator:
# # TypeError: 'NoneType' object is not callable
#
