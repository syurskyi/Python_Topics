"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(object):
    ___ isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ root __ N..
            r.. T..
        __ root.left __ N.. a.. root.right __ N..
            r.. T..
        __ root.left __ n.. N.. a.. root.right __ n.. N..
            r.. _isSymmetric(root.left, root.right)
        r.. F..

    ___ _isSymmetric(self, left, right):
        __ left __ N.. a.. right __ N..
            r.. T..
        __ left __ n.. N.. a.. right __ n.. N..
            r.. (left.val __ right.val a..
                    _isSymmetric(left.left, right.right) a..
                    _isSymmetric(left.right, right.left))
        r.. F..
