# class GetAttr
#     attr1 = 1
#
#     ___ - ____
#         ____.attr2 = 2
#
#     ___ -g ____ attr            # On undefined attrs only
#         print('get: ' + a..               # Not attr1: inherited from class
#         r_ 3                            # Not attr2: stored on instance
#
# X = ?
# print ?._1
# print ?._2
# print ?._3
#
# print('-'*40)
#
#
# c_ GetAttribute o..                 # (object) needed in 2.6 only
#     attr1 = 1
#
#     ___ - ____
#         ____.attr2 = 2
#
#     ___ -g ____ attr       # On all attr fetches
#         print('get: ' + a..               # Use superclass to avoid looping here
#         i_ a.. __ 'attr3':
#             r_ 3
#         e____
#             r_ obj_. -g ____ a..
#
#
# X = ?
# print ?._1
# print ?._2
# print ?._3
#
