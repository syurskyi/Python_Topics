# # Return Binary Pre-order Traversal
# # Question: Given a binary tree, return the preorder traversal of its nodes' values.
# # For example:
# # Given binary tree
# # 1
# # \
# # 2
# # /
# # 3
# # return [1,2,3].
# # Solutions:
#
# c_ TreeNode
#     ___  -  x
#         val _ x
#         left _ N..
#         right _ N..
#
# c_ Solution
#     ___ preorderTraversal root
#         result _   # list
#         stack _ ?
#
#         w___ stack
#             node _ ?.p..
#             __ ?
#                 ?.ap.. ?.v..
#                 ?.ap.. ?.r..
#                 ?.ap.. ?.l..
#         r_ ?
#
# __  -n __ ______
#     BT, BT.r.. BT.r__.l.. _ ? 1 ? 2 ? 3
#     print   ?.? B.