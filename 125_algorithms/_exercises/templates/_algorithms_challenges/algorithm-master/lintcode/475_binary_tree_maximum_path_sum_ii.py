"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    ___ maxPathSum2(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            r_ 0

        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)

        r_ root.val + max(0, left, right)
