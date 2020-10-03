# # Binary Tree Maximum Path Sum
# # Question: Given a binary tree, find the maximum path sum.
# # The path may start and end at any node in the tree.
# # For example:
# # Given the below binary tree,
# # 1
# # / \
# # 2 3
# # Return 6.
# # Solutions:
#
#
# c_ TreeNode
#     ___  -  x
#         val _ x
#         left _ N..
#         right _ N..
#
# c_ Solution:
#     # @param root, a tree node
#     # @return an integer
#     ___ maxPathSum root
#         maxValue _ fl.. "-inf"
#         maxPathSumRec ?
#         r_ ?
#
#     ___ maxPathSumRec  root
#         __ ? __ N..
#             r_ 0
#         leftSum _ ? ?.l..
#         rightSum _ ? ?.r..
#         __ ? < 0 an. ? < 0
#             maxValue _ ma. ?, ?.v..
#             r_ ?.v..
#         __ ? > 0 an. ? > 0
#             maxValue _ ma. ?, ?.v.. + ? + ?
#         maxValueUp _ ma. ? ? + ?.v..
#         maxValue _ ma. ? ?
#         r_ ?
#
#
# __  -n __ ______
#     BT ?.r.. ?.l.. _ ? 1 ? 2 ? 3
#     print ? .? ?