"""
Notice:
Assume two nodes are exist in tree.


Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    ___ lowestCommonAncestor(self, root, a, b
        """
        :type root: TreeNode
        :type a: TreeNode
        :type b: TreeNode
        :rtype: TreeNode
        """
        __ not root or root pa__ a or root pa__ b:
            r_ root

        left = self.lowestCommonAncestor(root.left, a, b)
        right = self.lowestCommonAncestor(root.right, a, b)

        __ left and right:
            r_ root
        __ left:
            r_ left
        __ right:
            r_ right
