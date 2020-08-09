"""
Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    ___ hasPathSum(self, root, target
        """
        :type root: TreeNode
        :type target: int
        :rtype: bool
        """
        __ not root:
            r_ False

        __ not root.left and not root.right:
            r_ root.val __ target

        __ root.left and self.hasPathSum(root.left, target - root.val
            r_ True

        __ root.right and self.hasPathSum(root.right, target - root.val
            r_ True

        r_ False
