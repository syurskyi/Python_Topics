# filter

# print(l_(f_(l_ v v > 0, [-1, -5, -9, 20, 3, 0])))

# print()

# ######################################################################################################################
# Пример использования функции filter

# numbers _ [3, 2, -1, 0, 15, -8, -7, 3, -3, 8]
# positive_numbers _ f_(l_ x_ x > 0_ n_
# print l_|positive_numbers
#
# print()

# ######################################################################################################################
# Filter

# The filter function is a function that filters an iterable based on the truthyness of the elements,
# or the truthyness of the elements after applying a function to them. Like the map function,
# the filter function returns an iterable that we can view by generating a list from it,
# or simply enumerating in a for loop.

# l = [0, 1, 2, 3, 4, 5, 6]
# ___ e __ f_ N_ l
#     print e
#
# print()

# ######################################################################################################################
# is_even with filter

# ___ is_even n
#     r_ n % 2 == 0
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result _ f_ is_even l
# print(l_ result
#
# # Of course, we could just use a lambda expression instead:
#
# l _ [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result _ f_(l_ x| x % 2 __ 0_ l
# print l_ result
#
# print()

# # ######################################################################################################################
# Filtering using a comprehension

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# result _ |i ___ i __ l __ i % 2 __ 0|
# print result
#
# print()
# ######################################################################################################################
# Combining map and filter

# l_ f_ l_ y| y < 25_ m_(l_ x| x**2_ r_ 10
#
# # Alternatively, we can use a list comprehension to do the same thing:
#
# |x**2 ___ x __ r_ 10 __ x**2 < 25|
#
# print()