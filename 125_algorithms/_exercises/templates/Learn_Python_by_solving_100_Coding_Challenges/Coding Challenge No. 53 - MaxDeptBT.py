# # Maximum Depth of Binary Tree
# # Question: Given a binary tree, find its maximum depth.
# # The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# # Solutions:
#
#
# c_ TreeNode
#     ___  -  x
#         val _ x
#         left _ N..
#         right _ N..
#
#
# c_ Solution
#     # @param root, a tree node
#     # @return an integer
#     ___ maxDepth_recursive  root
#         __ root __ N..
#             r_ 0
#         r_ ma. ? ?.l.. ? ?.r.. + 1
#
#     ___ maxDepth_interative  root
#         __ root __ N..
#             r_ 0
#         nodeStack _ ?
#         depthStack _ 1
#         maxDepth _ 0
#         w___ le. n.. > 0
#             node _ ?.p..
#             depth _ ?.p..
#             maxDepth _ ? __ ? > d.. ____ ?
#             __ ?.l.. !_ N..
#                 n__.ap.. ?.l..
#                 d__.ap.. ? + 1
#             __ ?.r.. !_ N..
#                 n__.ap.. ?.r..
#                 d__.ap.. ? + 1
#         r_ ?
#
#
# __  -n __ ______
#     BT ?.r.., ?.r...l.. _ ? 1 ? 2 ? 3
#     print   ? .? ?