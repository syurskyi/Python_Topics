# """
# "Descriptors" section example of descriptor that allows for lazy
# initialization of class instance attributes
#
# """
#
#
# c_ InitOnAccess
#     ___ - klass $  $
#         ?  ?
#         ?  ?
#         ?  ?
#         _initialized _ N..
#
#     ___ -g instance owner
#         __ no. _?
#             print('initialized!')
#             _? = k.... $ $$
#         ____
#             print('cached!')
#         r_ _?
#
#
# c_ MyClass
#     lazily_initialized _ I... li.. "argument"
#
# __ _______ __ _______
#     instance _ M...
#
#     print("First access to instance.lazily_initialized")
#     print(">> instance.lazily_initialized =", ?.l.. '\n')
#
#     print("Next access to instance.lazily_initialized")
#     print(">> instance.lazily_initialized =", ?.l... '\n')
