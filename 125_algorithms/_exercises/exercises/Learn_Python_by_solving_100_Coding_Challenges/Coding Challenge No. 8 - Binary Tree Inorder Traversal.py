# # Return Binary In-order Traversal
# # Question: Given a binary tree, return the inorder traversal of its nodes' values.
# # For example:
# # Given binary tree {1,2,3},
# # 1
# # \
# # 2
# # /
# # 3
# # return [1,3,2].
# # Solutions:
#
# c_ TreeNode
#     ___  -  x
#         val _ x
#         left _ N..
#         right _ N..
#
# c_ Solution
#     ___ inorderTraversal root
#         stack _   # list
#         node _ ?
#         solution _   # list
#         w___ ?!_ N.. o. le. s.. > 0
#             __ ? !_ N..
#                 s__.ap.. ?
#                 n.. _ ?.l..
#             ____
#                 node _ s__.p..
#                 s__.ap.. ?.v..
#                 node _ node.r..
#         r_ ?
#
# __  -n __ ______
#     BT B_.r.. B_.r__.l.. _ ? 1 ? 2 ? 3
#     print   ?.? B.