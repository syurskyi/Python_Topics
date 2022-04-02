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

c_ Solution(o..
    ___ isSameTree  p, q
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        __ p __ N.. a.. q __ N..
            r.. T..
        ____ p __ n.. N.. a.. q __ n.. N..
            __ (p.val __ q.val a..
                    isSameTree(p.left, q.left) a..
                    isSameTree(p.right, q.right)):
                r.. T..
        r.. F..
