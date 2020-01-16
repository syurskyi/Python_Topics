# c_ empty:
#     ___ -g ____ attrname
#         __ ? __ "age":
#             r_ 40
#         ____
#             r____ A... ?
# X = ?
# print(?.age)
#
# # X.name   # AttributeError: name
#
# c_ accesscontrol
#     ___ -s ____ attr value
#         __ a.. __ 'age'
#             ____.-d|a.. = v..
#         _____
#             r_____ A... a.. + ' not allowed'
# X = a...
# X.age = 40                                  # Calls __setattr__
# print(X.age)
# #
# # X.name = 'mel'  # AttributeError: name not allowed
# #
# #
# #
# c_ PrivateExc E.. p..                   # More on exceptions later
#
#
# c_ Privacy
#     ___ -s ____ attrname value         # On ____.attrname = value
#         __ a.. __ ____.privates
#             r.. P.. a... ____
#         _____
#             ____. -d a... _ v...        # ____.attrname = value loops!
#
#
# c_ Test1 P..
#     privates = age
#
#
# c_ Test2 P..
#     privates _ name pay
#     ___ -  ____
#         ____. -d|n.. _ 'Tom'
#
# x = _1
# y = _2
#
# x.name = 'Bob'
# print(x.name)
# # y.name = 'Sue'                                      # Fails
# #
# y.age = 30
# print(y.age)
# # x.age = 40                                         # Fails
# #
