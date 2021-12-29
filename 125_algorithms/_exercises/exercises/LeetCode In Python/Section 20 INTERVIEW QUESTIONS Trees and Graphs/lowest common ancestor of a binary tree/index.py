# # Definition for a binary tree node.
# # class TreeNode:
# #     ___ __init__(self, x
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# c_ Solution
#     ___ lowestCommonAncestor root 'TreeNode' p 'TreeNode' q 'TreeNode' 'TreeNode'
#         __ ? pa__ N..
#             r_ N..
#         __ ?.v.. __ ?.v.. o.. ?.v. __ ?.v..
#             r_ ?
#
#         left _ .? ?.l.. ? ?
#         right _ .? ?.r.. ? ?
#
#         __ ? pa__ N.. a.. ? pa__ N..
#             r_ N..
#         __ ? pa__ no. N.. a.. ? pa__ no. N..
#             r_ ?
#         __ ? pa__ N..
#             r_ ?
#         r_ ?