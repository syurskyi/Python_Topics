# a = {'k1': 100, 'k2': 200}
# print(a)
#
# print h.. 1, 2, 3
#
# # hash([1, 2, 3]) TypeError: unhashable type: 'list'
#
# print('#' * 52 + ' So we can create dictionaries that look like this: ')
#
# a = {('a', 100): ['a', 'b', 'c'], 'key2': {'a': 100, 'b': 200}}
# print(a)
#
# print('#' * 52 + ' Interestingly, functions are hashable: ')
#
# ___ my_func a, b, c
#     print(a, b, c)
#
# print(h.. ?
#
# print('#' * 52 + ' Which means we can use functions as keys in dictionaries: ')
# d = ? 10, 20, 30
# print ?
#
# print('#' * 52 + ' A simple application of this might be to store the argument values we want to use to call the '
#                  'function at a later time: ')
#
# ___ fn_add a, b
#     r_ a + b
#
# ___ fn_inv a
#     r_ 1/a
#
# ___ fn_mult a, b
#     r_ a * b
#
# funcs = {f._a. (10, 20 , f._i. (2,), f_m. 2, 8
# print ?
#
# print('#' * 52 + ' Remember that when we iterate through a dictionary we are actually iterating through the keys: ')
#
# ___ f in ?
#     print ?
#
# ___ f in ?
#     result = ? $? ?
#     print ?
#
# print('#' * 52 + ' We can also iterate through the items (as tuples) in a dictionary as follows: ')
#
# ___ f, args __ ?.it..
#     print ? a..
#
# ___ f, args __ ?.it..
#     result = ? $?
#     print ?
#
# print('#' * 52 + ' #### Using the class constructor ')
#
# d = di.. a=100, b=200)
# print ?
#
# print('#' * 52 + ' We can also build a dictionary by passing it an iterable containing the keys and the values: ')
#
# d = di.. 'a' 100 'b' 200
# print ?
#
# print('#' * 52 + ' The restriction here is that the elements of the iterable must themselves be iterables with exactly'
#                  ' two elements.  ')
#
# d = di.. 'a ', 100 , 'b' 200
# print(d)
#
# print('#' * 52 + ' Of course we can also pass a dictionary as well:  ')
#
# d = {'a': 100, 'b': 200, 'c': {'d': 1, 'e': 2}}
#
# print(id(d))
#
# print('#' * 52 + '  And lets create a dictionary: ')
#
# new_dict = dict(d)
# print(new_dict)
# print(id(new_dict))
#
# print('#' * 52 + '  As you can see, we have a new object - however, what about the nested dictionary? ')
#
# print(id(d['c']), id(new_dict['c']))
#
# print('#' * 52 + '  #### Using Comprehensions ')
#
# keys = ['a', 'b', 'c']
# values = (1, 2, 3)
#
# print('#' * 52 + '  We can then easily create a dictionary this way - the non-Pythonic way! ')
#
# d      # creates an empty dictionary
# ___ k, v __ z..  k.. v..
#     ? k _ v
#
# print(d)
#
# print('#' * 52 + ' But it is much simpler to use a dictionary comprehension:  ')
#
# d = k v ___ k, ? __ z.. k.. v..
# print ?
#
# print('#' * 52 + '  Dictionary comprehensions support the same syntax as list comprehensions - you can have'
#                  '  nested loops, `if` statements, etc. ')
#
# keys = ['a', 'b', 'c', 'd']
# values = (1, 2, 3, 4)
#
# d = k v ___ k, ? __ z.. k.. v.. i_ ? % 2 __ 0
# print ?
#
# print('#' * 52 + '  ')
#
# x_coords = (-2, -1, 0, 1, 2)
# y_coords = (-2, -1, 0, 1, 2)
#
# grid = [(x, y)
#          ___ x in x_coords
#          ___ y in y_coords]
# print(grid)
#
# print('#' * 52 + ' We can use the `math` modules `hypot` function to do calculate these distances ')
#
# import math
# print(math.hypot(1, 1))
#
# grid_extended = x, y, m__.hy.. x, y ___ x y i. g..
# print ?
#
# print('#' * 52 + ' We can now easily tweak this to make a dictionary, where the coordinate pairs are the key, '
#                  ' and the distance the value: ')
#
# grid_extended = x, y  ma__.hy.. x, y ___ x, y i_ g..
# print ?
#
# print('#' * 52 + '  #### Using `fromkeys` ')
# print('#' * 52 + ' The `dict` class also provides the `fromkeys` method that we can use to create dictionaries.'
#                  ' This class method is used to create a dictionary from an iterable containing the keys, and'
#                  ' a **single** value used to assign to each key. ')
#
# counters = di__.f.k. 'a', 'b', 'c'], 0)
# print ?
#
# print('#' * 52 + ' If we do not specify a value, then `None` is used:  ')
#
# d = di__.f_k_ abc
# print ?
#
# print('#' * 52 + ' Notice how I used the fact that strings are iterables to specify the three single character '
#                  'keys ___ this dictionary!  ')
# print('#' * 52 + ' `fromkeys` method will insert the keys in the order in which they are retrieved from the iterable: ')
#
# d = di__.f..k.. python
# print ?
# print((?))
