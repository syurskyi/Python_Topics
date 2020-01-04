# partial

# _____ f_ _____ ____
#
# # Частичное применение функции
# print_with_comma = p... print s_-', '
#
# ? 2 3 5
#
# print()

# ######################################################################################################################
# Partial Functions

# _____ fu_ ______ _____
# ___ my_func a b c
#     print a b c
# f _ p_ my_func 10
# f 20 30
#
# # We could have done this using another function (or a lambda) as well:
#
# ___ partial_func b c
#     r_ my_func 10 b c
#
# # or, using a lambda:
#
# fn _ l_ b_ c| my_func 10 b c
# fn 20 30
#
# print()
# ######################################################################################################################
# Partial Functions
# it is quite flexible with parameters:

# ___ my_func a b _args k1 k2 __kwargs
#     print a b args k1 k2 kwargs
#
# f - p_ my_func 10 k1-|a|
# f 20 30 40 k2-|b| k3-|c|
#
# # We can of course do the same thing using a regular function too:
#
# ___ f b _args k2 __kwargs
#     r_ my_func 10 b _args k1_|a| k2_k2 __kwargs
#
# f 20 30 40 k2_|b| k3_|c|
#
# print()
# ######################################################################################################################
# Partial Functions
# you are not stuck having to specify the first argument in your partial:

# ___ power base exponent
#     r_ base ** exponent
#
# power 2 3
# square _ p_ power exponent_2
# square 4
# cube _ p_ power exponent_3
# cube 2
#
# cube base_3
#
# print()