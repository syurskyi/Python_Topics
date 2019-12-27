# c_ AttrSquare
#     ___ - ____ start
#         ____.value = start  # Triggers __setattr__!
#
#     ___ -g ____ attr  # On undefined attr fetch
#         i_ a.. __ 'X':
#             r_ ____.v.. ** 2  # value is not undefined
#         e____
#             r____ A.... a..
#
#     ___ -s ____ attr value  # On all attr assignments
#         i_ a.. __ 'X'
#             attr _ 'value'
#         ____. -d a.. _ v..
#
#
# A _ ? 3  # 2 instances of class with overloading
# B _ ? 32  # Each has different state information
#
# print(A.X)  # 3 ** 2
# A.X = 4
# print(A.X)  # 4 ** 2
# print(B.X)  # 32 ** 2
#
#
# c_ AttrSquare
#     ___ - ____ start
#         ____.value _ s..  # Triggers __setattr__!
#
#     ___ -g ____ attr  # On all attr fetches
#         i_ a.. __ 'X'
#             r_ ____.va.. ** 2  # Triggers __getattribute__ again!
#         e____
#             r_ obj__. -g ____ a..
#
#     ___ -s  ____ attr value  # On all attr assignments
#         i_ a... __ 'X'
#             a.. _ 'value'
#         obj__. -s  ____ a.. v..
#
#     ___ -g ____ attr
#         i_ attr __ 'X':
#             r_ obj___. -g ____ 'value') ** 2
#
#
