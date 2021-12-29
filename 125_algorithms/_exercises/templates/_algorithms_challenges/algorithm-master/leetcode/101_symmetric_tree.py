"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    ___ isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root:
            r.. True

        r.. self.divide_conquer(root.left, root.right)

    ___ divide_conquer(self, left, right):
        __ n.. left a.. n.. right:
            r.. True
        __ n.. left o. n.. right:
            r.. False
        __ left.val != right.val:
            r.. False
        __ n.. self.divide_conquer(left.left, right.right):
            r.. False
        __ n.. self.divide_conquer(left.right, right.left):
            r.. False
        r.. True
