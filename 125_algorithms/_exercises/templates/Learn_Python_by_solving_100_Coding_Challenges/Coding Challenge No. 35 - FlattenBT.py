# # Flatten Binary Tree
# # Question: Given a binary tree, flatten it to a linked list in-place.
# # For example:
# # Given
# # 1
# # / \
# # 2 5
# # / \ \
# # 3 4 6
# # The flattened tree should look like:
# # 1 \ 2 \ 3 \ 4 \ 5 \ 6
# # Solutions:
#
#
# c_ TreeNode
#     ___  -  x
#         val _ x
#         left _ N..
#         right _ N..
#
# c_ Solution
#     # @param root, a tree node
#     # @return nothing, do it in place
#     ___ flatten  root
#         __ root __ N..
#             r_
#         stack _ ?.r.. ?.l..
#         current _ ?
#         w___ le. s.. !_ 0
#             nextNode _ s__.p..
#             __ ? __ N..
#                 c..
#             ____
#                 ?.l.. _ N..
#                 ?.r.. _ n..
#                 current _ ?.r..
#                 s__.ap.. ?.r..
#                 s__.ap.. ?.l..
#
#         r_ ?
#
#         ___ printtree tree_node
#             __ ?.l.. i. no. N..
#                 ? ?.l..
#             print ?.v..
#         __ ?.r.. i. no. N..
#             ? ?.r..
#
#
# __  -n __ ______
#     BT ?.r__, ?.r__.r__, ?.l__, ?.l__.r__, ?.l__.l__ _ ? 1 ? 5 ? 6 ? 2 ? 4 ? 3
#     LL _ ? .? ?
#     ? .? ?