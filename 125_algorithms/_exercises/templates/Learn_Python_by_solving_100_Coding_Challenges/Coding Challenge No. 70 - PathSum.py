# # Path Sum
# # Question: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# # For example: Given the below binary tree and sum = 22,
# # 5
# # / \
# # 4 8
# # / / \
# # 11 13 4
# # / \ \
# # 7 2 1
# # return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
#     # @param sum, an integer
#     # @return a boolean
#     ___ hasPathSum  root su.
#         __ ? __ N..
#             # Empty tree will always result in False
#             r_ F..
#         ____ ?.l.. __ N.. an. ?.r.. __ N..
#             # Reach the leaf.
#             r_ ?.v.. __ su.
#         ____ ?.l.. __ N..
#             # Only has right child.
#             r_ ? ?.r.., su.-?.v..
#         ____ ?.r.. __ N..
#             # Only has left child.
#             r_ ? ?.l.., su.-?.v..
#         ____
#             # Has two children.
#             r_ ? ?.l.. su.-?.v.. o. ? ?.r.. su.-?.v..
#
#
# __  -n __ ______
#     BT ?.r.., ?.r...l.., ?.l.. _ ? 1 ? 2 ? 3 ? 10
#     print ?.? ? 6