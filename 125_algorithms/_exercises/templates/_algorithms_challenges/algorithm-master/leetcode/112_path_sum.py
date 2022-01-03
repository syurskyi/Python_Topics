"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


c_ Solution:
    ___ hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: bool
        """
        __ n.. root:
            r.. F..

        __ n.. root.left a.. n.. root.right:
            r.. root.val __ target

        __ root.left a.. hasPathSum(root.left, target - root.val):
            r.. T..

        __ root.right a.. hasPathSum(root.right, target - root.val):
            r.. T..

        r.. F..
