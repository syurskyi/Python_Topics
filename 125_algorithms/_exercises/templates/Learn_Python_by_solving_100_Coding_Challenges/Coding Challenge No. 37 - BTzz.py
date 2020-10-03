# # Return binary zigzag level order traversal
# # Question: Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# # For example: Given binary tree {3,9,20,#,#,15,7},
# # 3
# # / \
# # 9 20
# # / \
# # 15 7
# # return its zigzag level order traversal as:
# # [ [3], [20,9], [15,7] ]
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
#     # @return a list of lists of integers
#     ___ zigzagLevelOrder root
#         solution _   # list
#         thisLevel _  # list
#         __ ? !_ N..
#             t__.ap.. ?
#         leftToRight _ T..
#         w___ le. t.. > 0
#             levelSolution _   # list
#             nextLevel _   # list
#             w___ le. t.. > 0
#                 node _ t__.p..
#                 l__.ap.. ?.v..
#                 __ l..
#                     __ ?.l.. !_ N..
#                         n__.ap.. ?.l..
#                     __ ?.r.. !_ N..
#                         n__.ap.. ?.r..
#                 ____
#                     __ ?.r.. !_ N..
#                         n__.ap.. ?.r..
#                     __ ?.l.. !_ N..
#                         n__.ap.. ?.l..
#             thisLevel _ n..
#             s__.ap.. l..
#             l.. _ no. l..
#         r_ ?
#
#
# __  -n __ ______
#     BT, ?.l.. ?.r.. ?.r__.l.. ?.r__.r.. _ ? 3 ? 9 ? 20 ? 15 ? 7
#     print ? .? ?