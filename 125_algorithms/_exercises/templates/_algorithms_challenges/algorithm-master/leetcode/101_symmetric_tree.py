"""
Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    ___ isSymmetric(self, root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ not root:
            r_ True

        r_ self.divide_conquer(root.left, root.right)

    ___ divide_conquer(self, left, right
        __ not left and not right:
            r_ True
        __ not left or not right:
            r_ False
        __ left.val != right.val:
            r_ False
        __ not self.divide_conquer(left.left, right.right
            r_ False
        __ not self.divide_conquer(left.right, right.left
            r_ False
        r_ True
