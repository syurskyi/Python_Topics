"""
Premium Question
"""
__author__ = 'Daniel'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ___ inorderSuccessor(self, root, p):
        """
        search

        If it is a general binary tree
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        find = [None]
        self.search(root, p, find)
        return find[0]

    ___ search(self, cur, p, find):
        __ not cur:
            return

        __ cur.val > p.val:
            find[0] = cur
            self.search(cur.left, p, find)
        else:
            self.search(cur.right, p, find)