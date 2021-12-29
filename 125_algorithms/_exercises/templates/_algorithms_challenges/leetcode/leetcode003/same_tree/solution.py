"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and
the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ___ isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        __ p is None and q is None:
            return True
        elif p is not None and q is not None:
            __ (p.val == q.val and
                    self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right)):
                return True
        return False
