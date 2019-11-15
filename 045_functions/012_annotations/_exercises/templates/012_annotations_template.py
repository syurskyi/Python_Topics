# # ######################################################################################################################
# Annotations

# ___ my_func a: 'annotation for a'
#             b: 'annotation for b') __ 'annotation for return':
#     r_ a * b
#
# help my_func
#
# print()
# ######################################################################################################################
# The annotations can be any expression, not just strings:

# x = 3
# y = 5
# ___ my_func a| s_ __ 'a repeated ' + s_(m_(3, 5)) + ' times':
# 	r_ a*max x y
#
# help my_func
#
# print()
# ######################################################################################################################
# Just like docstrings are stored in the __doc__ property, annotations are stored in the __annotations__ property -
# a dictionary whose keys are the parameter names, and values are the annotation.

# x = 3
# y = 5
# ___ my_func a| s_ __ 'a repeated ' + s_(m_(3, 5)) + ' times':
# 	r_ a*max x y
#
# my_func.__a_
#
# print()
# ######################################################################################################################
# Annotations will work with default parameters too: just specify the default after the annotation

# ___ my_func a|str_'a' b|int_1)__s_
#     r_ a*b
#
# help my_func
# my_func()
# my_func abc 3
#
# ___ my_func a|i_-0 _args|additional args
#     print a args
#
# my_func.__a_
#
# help my_func
#
# print()


# ######################################################################################################################
# Map

# The map built-in function is a higher-order function that applies a function to an iterable type object:

# ___ fact n
#     r_ 1 __ n < 2 ____ n * fact(n-1)
#
# fact 3
# fact 4
#
# m_(fact_ |1 2 3 4 5|
#
# # The map function returns a map object, which is an iterable - we can either convert that to a list or enumerate it:
#
# l _ l_(m_(fact_ |1 2 3 4 5|
# print l
#
# # We can also use it this way:
#
# l1 _ [1, 2, 3, 4, 5]
# l2 _ [10, 20, 30, 40, 50]
#
# f _ l_ x y| x+y
#
# m _ m_ f l1 l2
# l_ m
#
# print()