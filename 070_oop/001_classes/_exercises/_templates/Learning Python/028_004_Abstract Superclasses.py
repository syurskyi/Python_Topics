# c_ Super
#     ___ delegate ___
#         ___.action
#     ___ ? ___
#         a... F.. 'action must be defined!'         # If this version called
#
#
# X = ?
# # X.delegate()
# # AssertionError: action must be defined!
#
# c_ Super:
#     ___ delegate ___
#         ___.action
#     ___ ? ___
#         r... N.. action must be defined!
#
#
# X = ?
# # X.delegate()
# # NotImplementedError: action must be defined!
#
#
# c_ Sub ?
#     p..
#
#
# X = Su.
# # X.delegate()
# # NotImplementedError: action must be defined!
#
#
# c_ Sub ?
#     ___ action ___ print('spam')
#
# X = S..
# ?.d..
#
