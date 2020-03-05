# """
# "Using the __new__() method to override instance creation process" section
# example of overriding `__new__()` method when subclassing non-mutable
# Python built-in types.
#
# """
#
#
# c_ NonZero int
#     ___ -n ___ value
#         r_ s___ . -n ___ ? __ ? !_ 0 ____ N...
#
#     ___ - skipped_value
#         # implementation of __init__ could be skipped in this case
#         # but it is left to present how it may be not called
#         print("__init__() called")
#         s___ . -
#
#
# __ _______ __ _______
#     print("NonZero(-12)    =" ? -12
#     print("NonZero(-3.123) =" ? -3.123
#     print("NonZero(0)      =" ? 0
#
