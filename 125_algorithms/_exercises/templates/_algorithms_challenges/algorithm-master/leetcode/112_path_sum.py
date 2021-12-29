"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    ___ hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: bool
        """
        __ n.. root:
            r.. False

        __ n.. root.left and n.. root.right:
            r.. root.val __ target

        __ root.left and self.hasPathSum(root.left, target - root.val):
            r.. True

        __ root.right and self.hasPathSum(root.right, target - root.val):
            r.. True

        r.. False
