# # Annotations
#
# ___ my_func a annotation for a
#             b 'annotation for b __ annotation for return
#     r_ a * b
#
#
# help m...
#
# # The annotations can be any expression, not just strings:
#
# x = 3
# y = 5
# ___ my_func a str __ *a repeated * + s.. ma. 3 5 + * times
# 	r_ a*m.. x y
#
# help m..
#
# # Just like docstrings are stored in the __doc__ property, annotations are stored in the __annotations__ property
# # - a dictionary whose keys are the parameter names, and values are the annotation.
#
# x = 3
# y = 5
# ___ my_func a: str __ *a repeated * + s.. ma. 3 5 + * times
# 	r_ a*m.. x y
#
# m._f_.__a....
#
# # Annotations will work with default parameters too: just specify the default after the annotation
#
# ___ my_func a; s.._ a  b; i.._1 __s..
#     r_ a*b
#
# help m...
# m...
# m... 'abc' 3
#
# ___ my_func a; i.._0 0a...; *additional args
#     print a a...
#
# m._f_.__a....
#
# help m....
#
# # Function Introspection
# # The name attribute holds the function's name:
#
# ___ my_func a b_2 c_3 * kw1 kw2_2 00k...
#     pa..
#
# f _ m...
#
#
# m___.__n____
# f.__n____
#
# # Function Introspection
# # The defaults attribute is a tuple containing any positional parameter defaults:
#
# ___ my_func a b_2 c_3 * kw1 kw2_2 00k___
#     p...
# f _ m...
#
# m___.__de_____
# m____.__kw____
#
#
# # Function Introspection
# # The code attribute contains a code object:
#
# ___ my_func a b_1 0ar.. 00k...
#     i _ 10
#     b _ min i b
#     r_ a * b
#
# m... 'a' 100
#
# m____.__c___
#
# d__ m____.__c___
#
# # Function Introspection
# #
# # Attribute co_varnames is a tuple containing the parameter names and local variables:
#
# ___ my_func a b_2 c_3 * kw1 kw2_2 00k...
#     pa..
#
# f _ m....
#
# m____.__c__.c._va..
#
#
# # Function Introspection
# # Attribute co_argcount returns the number of arguments (minus any * and ** args)
#
# ___ my_func a b_2 c_3 * kw1 kw2_2 00k___
#     pa..
#
# f _ m...
# m___.__c___.c._ar...
#
# # The inspect module
#
# ___ my_func a b_1 0a... 00k...
#     i _ 10
#     b _ min i b
#     r_ a * b
#
# m.... 'a' 100
#
# ______ i.....
# i___.isf.... m...
# i___.ism m....
#
# # Introspecting Callable Code
#
# ___ fact n| "some non-negative integer") -> "n! or 0 if n < 0": """Calculates the factorial of a non-negative integer n
#
# If n is negative, returns 0.
# """
# i_ n < 0:
#     r_ 0
# e____ n <= 1:
#     r_ 1
# e____
#     r_ n * fact(n-1)
#
# i___.getsource(fact)
#
#
#
#
#
