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
        __ not root:
            return True

        return self.divide_conquer(root.left, root.right)

    ___ divide_conquer(self, left, right):
        __ not left and not right:
            return True
        __ not left or not right:
            return False
        __ left.val != right.val:
            return False
        __ not self.divide_conquer(left.left, right.right):
            return False
        __ not self.divide_conquer(left.right, right.left):
            return False
        return True
