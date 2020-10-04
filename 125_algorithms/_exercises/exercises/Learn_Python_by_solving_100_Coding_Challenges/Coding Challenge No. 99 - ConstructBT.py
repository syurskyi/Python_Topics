# # Construct Binary tree
# # Question: Given inorder and postorder traversal of a tree, construct the binary tree.
# # Note: You may assume that duplicates do not exist in the tree.
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
#     # @param inorder, a list of integers
#     # @param postorder, a list of integers
#     # @return a tree node
#     ___ buildTree  inorder postorder
#         __ no. i..
#             r_ N.. # inorder is empty
#         ? ? _ ? ?
#         r_ ? 0 0 le. ?
#
#     ___ dfs  inLeft postLeft Len
#         __ L.. <_ 0
#             r_ N..
#         root _ ? p.. ? + ? - 1
#         rootPos _ ?.i.. p.. ? + ? - 1
#         ?.l.. _ ? ? ? rP.. - iL..
#         ?.r.. _ ? rP.. + 1 pL.. + rP.. - iL.. L.. - 1 -  rP.. - i..
#         r_ ?
#
#
# ? .? [1,3,2],[3,2,1]