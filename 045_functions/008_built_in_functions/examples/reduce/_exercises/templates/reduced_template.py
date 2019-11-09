# filter

# print(l_(f_(l_ v v > 0, [-1, -5, -9, 20, 3, 0])))

# print()

# ######################################################################################################################
# Пример использования функции reduce

# f_ f_ _____ r_
#
# numbers _ [3, 2, 1, 8, -3, -2]
# # Произведение всех чисел списка
# product _ r_ l_ x_ y_ x * y, numbers
#
# print(product)
#
# print()

# ######################################################################################################################
# Maximum and Minimum
# Using Reducing Functions
#
# l = [5, 8, 6, 10, 9]
# _max = l_ a_ b| a __ a > b e_ b
# _min = l_ a_ b| a __ a < b e_ b
#
# ___ _reduce fn sequence
#     result _ sequence|0|
#     ___ x __ sequence|1_|
#         result _ fn result x
#     r_ result
#
# _reduce _max l
# _reduce _min l

# We could even just use a lambda directly in the call to _reduce:
#
# _reduce(l_ a_ b| a __ a > b e_ b_ l
# _reduce(l_ a_ b| a __ a < b e_ b_ l
#
# print()
# ######################################################################################################################
# Python actually implements a reduce function, which is found in the functools module.
# Unlike our _reduce function, it can handle any iterable, not just sequences.

# f_ f_ i_ r_
# l = [5, 8, 6, 10, 9]
# l
# r_(l_ a_ b| a __ a > b e_ b_ l)
# r_(l_ a_ b| a __ a < b e_ b_ l)
# r_(l_ a_ b| a __ a < b e_ b_ l)
# r_(l_ a_ b| a + b_ l)
#
# print()
# ######################################################################################################################
# Finding the max and min of an iterable is such a common thing that Python provides a built-in function to do just that:

# l = [5, 8, 6, 10, 9]
# m_ l, m_ l
# s_ l
#
# print()
# # ######################################################################################################################
# The any and all built-ins
#
# l = [0, 1, 2]
# a_ l
#
# l = [0, 0, 0]
# a_ l
#
# print()
# ######################################################################################################################
# On the other hand, all will return True if every element of the iterable is truthy:

# l = [0, 1, 2]
# a_(l)
#
# l = [1, 2, 3]
# a_(l)
#
# print()
# ######################################################################################################################
# We can implement any functions ourselves using reduce if we choose to - simply use the Boolean or or and operators as
# the function passed to reduce to implement any and all respectively.

# l = [0, 1, 2]
# r_(l_ a_ b| b_(a o_ b)_ l)
#
# l = [0, 0, 0]
# r_(l_ a_ b| b_(a o_ b)_ l)
#
# print()
# ######################################################################################################################
# We can implement all functions ourselves using reduce if we choose to - simply use the Boolean or or and operators as
# the function passed to reduce to implement any and all respectively.

# l = [0, 1, 2]
# r_(l_ a_ b| b_(a a_ b)_ l)
#
# l = [1, 2, 3]
# r_(l_ a_ b| b_(a a_ b)_ l)
#
# print()