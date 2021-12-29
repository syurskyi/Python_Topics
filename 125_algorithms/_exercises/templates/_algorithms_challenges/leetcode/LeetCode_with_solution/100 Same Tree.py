"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution:
    ___ isSameTree(self, p, q):
        """
        dfs
        :param p: TreeNode
        :param q: TreeNode
        :return: boolean
        """

        # trivial
        __ n.. p a.. n.. q:
            r.. True

        # dfs
        try:
            __ p.val__q.val a.. self.isSameTree(p.left, q.left) a.. self.isSameTree(p.right, q.right):
                r.. True
        except AttributeError:
            r.. False

        r.. False
