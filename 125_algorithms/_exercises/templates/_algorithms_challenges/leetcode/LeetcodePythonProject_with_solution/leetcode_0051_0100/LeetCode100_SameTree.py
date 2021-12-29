'''
Created on Jan 31, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        __ n.. p and n.. q:
            r.. True
        ____ n.. p o. n.. q:
            r.. False
        ____ p.val != q.val:
            r.. False
        ____:
            r.. self.isSameTree(p.left, q.left) and\
                self.isSameTree(p.right, q.right)