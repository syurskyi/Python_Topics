# # Recover Binary Search Tree
# # Question: Two elements of a binary search tree (BST) are swapped by mistake.
# # Recover the tree without changing its structure.
# # Note: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
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
#     # @return a tree node
#     ___ FindTwoNodes  root
#         __ ?
#             ? ?.l..
#             __ prev an. prev.v.. > ?.v..
#                 n2 _ ?
#                 __ n1 __ N..
#                     n1 _ p..
#                 p.. _ ?
#                 ? ?.r..
#
#     ___ recoverTree  root
#         n1 _ n2 _ N..
#         prev _ N..
#         ? ?
#         ?.v.. ?.v.. _ ?.v.. ?.v..
#         r_ ?