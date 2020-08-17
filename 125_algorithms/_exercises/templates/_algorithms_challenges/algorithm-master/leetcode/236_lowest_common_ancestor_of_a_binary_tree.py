# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object
    ___ lowestCommonAncestor(self, root, p, q
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        __ not root or root pa__ p or root pa__ q:
            r_ root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        __ left and right:
            r_ root
        __ left:
            r_ left
        __ right:
            r_ right
