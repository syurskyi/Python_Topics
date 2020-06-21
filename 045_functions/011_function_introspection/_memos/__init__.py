# ######################################################################################################################
# Function Introspection
# The name attribute holds the function's name:

# ___ my_func a b_2 c_3 _, kw kw2_2 __kwargs
#     pass
#
# f _ my_func
#
# my_func.__n_
# f.__n_
#
# print()
# ######################################################################################################################
# Function Introspection
# The defaults attribute is a tuple containing any positional parameter defaults:

# ___ my_func a b_2 c_3 _, kw1 kw2_2 __kwargs
#     pass
# f _ my_func
#
# my_func.__d_
# my_func.__k_
#
# print()
# ######################################################################################################################
# Function Introspection
# The code attribute contains a code object:

# ___ my_func a b_1 _args __kwargs
#     i _ 10
#     b _ m_ i b
#     r_ a * b
#
# my_func |a| 100
#
# my_func.__c_
#
# d_ my_func.__c_
#
# print()
# ######################################################################################################################
# Function Introspection
#
# Attribute co_varnames is a tuple containing the parameter names and local variables:

# ___ my_func a b_2 c_3 _, kw1 kw2_2 __kwargs
#     pass
#
# f = my_func
#
# my_func.__c_.c__v_
#
# print()
# ######################################################################################################################
# Function Introspection
# Attribute co_argcount returns the number of arguments (minus any * and ** args)

# ___ my_func a b_2 c_3 _, kw1 kw2_2 __kwargs
#     pass
#
# f _ my_func
# my_func.__c_.c__a_
#
# print()
# ######################################################################################################################
# The inspect module

# ___ my_func a b_1 _args __kwargs
#     i _ 10
#     b _ m_ i b
#     r_ a * b
#
# my_func |a| 100
#
# i_ i_
# i_.i_f_ my_func
# inspect.i_m_my_func
#
# print()
# ######################################################################################################################
# Introspecting Callable Code
#
# ___ fact(n: "some non-negative integer") -> "n! or 0 if n < 0": """Calculates the factorial of a non-negative integer n
#
# If n is negative, returns 0.
# """
# __ n < 0
#     r_ 0
# ____ n <= 1
#     r_ 1
# ___
#     r_ n * fact(n-1)
#
# i_.g_(f_)
#
# print()