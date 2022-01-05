"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


c_ Solution:
    ___ isSymmetric  root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root:
            r.. T..

        r.. divide_conquer(root.left, root.right)

    ___ divide_conquer  left, right):
        __ n.. left a.. n.. right:
            r.. T..
        __ n.. left o. n.. right:
            r.. F..
        __ left.val != right.val:
            r.. F..
        __ n.. divide_conquer(left.left, right.right):
            r.. F..
        __ n.. divide_conquer(left.right, right.left):
            r.. F..
        r.. T..
