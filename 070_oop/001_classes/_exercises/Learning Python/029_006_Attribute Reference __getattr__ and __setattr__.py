# c_ empty:
#     ___ -g ____ attrname
#         i_ attrname __ "age":
#             r_ 40
#         e___
#             r____ A... ?
# X = ?
# print(?.age)
#
# # X.name   # AttributeError: name
#
# c_ accesscontrol
#     ___ -s ____ attr value
#         i_ a.. __ 'age'
#             ____.-d a.. = v..
#         e____
#             r_____ A... a.. + ' not allowed'
# X = a...
# X.age = 40                                  # Calls __setattr__
# print(X.age)
# #
# # X.name = 'mel'  # AttributeError: name not allowed
# #
# #
# #
#
#
# c_ PrivateExc E.. p..                   # More on exceptions later
#
#
# c_ Privacy
#     ___ -s ____ attrname value         # On ____.attrname = value
#         i_ a.. i_ ____.privates
#             r.. P.. a... ____
#         e____
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
#         ____. -d name _ 'Tom'
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
