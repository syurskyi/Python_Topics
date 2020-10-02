# # Return Binary Post-order Traversal
# # Question: Given a binary tree, return the postorder traversal of its nodes' values.
# # For example:
# # Given binary tree {1,2,3},
# # 1
# # \
# # 2
# # /
# # 3
# # return [3,2,1].
# # Solutions:
#
# c_ TreeNode
#     ___  -  x
#         val _ x
#         left _ N..
#         right _ N..
#
# c_ Solution
#     ___ postorderTraversal root
#         __ root __ N..
#             r_   # list
#         stackPrepare _ ?
#         stackReady _   # list
#         result _   # list
#         w___ le. s.. !_ 0
#             current _ s__.p..
#             s__.ap.. ?
#             __ ?.left !_ N.. s__.ap.. ?.l..
#             __ ?.right !_ N.. s__.ap.. ?.r..
#         w___ le. s.. !_ 0
#             ?.ap.. s__.p.. .v..
#         r_ ?
#
# __  -n __ ______
#     BT ?.r.. ?.r__.l.. _ ? 1 ? 2 ? 3
#     print   ?.? ?