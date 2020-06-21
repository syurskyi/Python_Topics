# # We have stated previously that Python's super() function allows us to refer to the superclass implicitly.
# #
# # But in the scenario of multi-level inheritances, which class will it refer to? Well, the super() function will
# # always refer to an immediate superclass.
# #
# # Also, a Python super() function not only can refer to the __init()__ function but also can call all other function
# # of a superclass.
# #
# # See the following example.
#
# # app.py
#
# c_ A:
#     ___ __init__
#         print('Initializing: class A')
#
#     ___ sub_method  b
#         print('Printing from class A:' ?
#
#
# c_ B A
#     ___ -
#         print('Initializing: class B')
#         s___. -
#
#     ___ sub_method  b
#         print('Printing from class B:' ?
#         s__.s_m.. ? + 1
#
#
# c_ C B
#     ___ -
#         print('Initializing: class C')
#         s__. -
#
#     ___ sub_method b
#         print('Printing from class C:' ?
#         s__.s_m.. ? + 1
#
#
# __ _____ __ ______
#     c = ?
#     >.s_m... 1
#
# # See the output below.
# #
# # Super() Method Tutorial Example
# # So, from the output, we can see that the __init()__ function of class C had been called at first,
# # then class B and after that class A.
# # The same thing happened by calling the sub_method() function.
# # If your program contains the multi-level inheritance, then the super() function is beneficial for you as well.
#
