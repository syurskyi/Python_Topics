# # Minimum Depth of Binary Tree
# # Question: Given a binary tree, find its minimum depth.
# # The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
#     ___ minDepth  root
#         __ ? __ N..
#             r_ 0
#         __ ?.l.. __ N..
#             r_ ? ?.r.. + 1
#         __ ?.r.. __ N..
#             r_ ? ?.l.. + 1
#         r_ mi. ? ?.l.. ? ?.r..+1
#
#
# __  -n __ ______
#     BT ?.r.. ?.r...l.. ?.l.. _ ? 1 ? 2 ? 3 ? 10
#     print   ? .? ?