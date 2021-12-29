"""
Premium Question
"""
__author__ = 'Daniel'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ inorderSuccessor(self, root, p):
        """
        search

        If it is a general binary tree
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        find = [N..]
        self.search(root, p, find)
        r.. find[0]

    ___ search(self, cur, p, find):
        __ n.. cur:
            r..

        __ cur.val > p.val:
            find[0] = cur
            self.search(cur.left, p, find)
        ____:
            self.search(cur.right, p, find)