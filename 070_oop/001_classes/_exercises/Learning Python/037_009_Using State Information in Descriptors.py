# c_ DescState:                           # Use descriptor state
#     ___ - ____, value
#         ____.v... _ v...
#     ___ -g ____ instance owner    # On attr fetch
#         print('DescState get')
#         r_ ____.v... * 10
#     ___ -s ____ instance v...    # On attr assign
#         print('DescState set')
#         ____.v... _ v...
#
# # Client class
#
# c_ CalcAttrs
#     X _ D___ 2                       # Descriptor c_ attr
#     Y _ 3                                  # Class attr
#     ___ - ____
#         ____.Z _ 4                         # Instance attr
#
# obj _ C...
# print(?.X, ?.Y, ?.Z)                 # X is computed, others are not
# ?.X _ 5                                  # X assignment is intercepted
# ?.Y _ 6
# ?.Z _ 7
# print(?.X, ?.Y, ?.Z)
#
#
# c_ InstState                           # Using instance state
#     ___ -g ____ instance owner
#         print('InstState get')             # Assume set by client class
#         r_ in___._Y * 100
#     ___ - ____ instance v...
#         print('InstState set')
#         in___._Y _ v...
#
# # Client class
#
# c_ CalcAttrs
#     X = D.. 2                       # Descriptor class attr
#     Y = I...                        # Descriptor class attr
#     ___ -  ____
#         ____._Y = 3                        # Instance attr
#         ____.Z  = 4                        # Instance attr
#
# obj = C..
# print(?.X, ?.Y, ?.Z)                 # X and Y are computed, Z is not
# ?.X _ 5                                  # X and Y arssignments intercepted
# ?.Y _ 6
# ?.Z _ 7
# print(?.X, ?.Y, ?.Z)
