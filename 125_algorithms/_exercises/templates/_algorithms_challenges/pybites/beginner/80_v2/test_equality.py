# ____ ? _______ ?, ?
#
#
# ___ test_same_reference
#     a = [1, 2, 3, 4]
#     b = a
#     # shallow copy (do not change original), alternatively use the copy module
#     c = a |
#     ... ? ? ? __ ?.S_R
#     ... ? ? ? != ?.S_R
#
#
# ___ test_same_ordered
#     a = [1, 2, 3, 4]
#     b = a |
#     c = a
#     ... ? ? ? __ ?.S_O
#     ... ? ? ? != ?.S_O  # SAME_REFERENCE
#
#
# ___ test_same_unordered
#     a = [1, 2, 3, 4]
#     b = a[::-1]
#     c = b |  + [5]
#     ... ? ? ? __ ?.S_U
#     ... ? ? ? != ?.S_U
#
#
# ___ test_same_unordered_deduped
#     a = [1, 2, 2, 3, 4]
#     b = a |  + [1, 3, 4, 4]
#     c = b |  + [5]
#     ... ? ? ? __ ?._U_D
#     ... ? ? ? != ?._U_D
#
#
# ___ test_not_same
#     a = [1, 2, 3]
#     b = [4, 5, 6]
#     ... ? ? ? __ ?.N..
