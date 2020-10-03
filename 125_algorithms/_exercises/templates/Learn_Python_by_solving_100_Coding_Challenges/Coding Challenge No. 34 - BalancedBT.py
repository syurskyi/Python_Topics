# # Balanced Binary Tree
# # Question: Given a binary tree, determine if it is height-balanced.
# # For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1
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
#     # @return a boolean
#     ___ isBalanced  root
#         r_ ? ? > _ 0
#
#     ___ isBalancedInt  root
#         __ root __ N..
#             r_ 0
#         l.. _ ? ?.l..
#         r.. _ ? ?.r..
#         __ ? < 0 o. ? < 0 o. ab. ? - ? > 1
#             r_ -1
#         r_ ma. ? ? + 1
#
# __  -n __ ______
#     BT ?.r.. ?.r__.l.. _ ? 1 ? 2 ? 3
#     print ? .? ?