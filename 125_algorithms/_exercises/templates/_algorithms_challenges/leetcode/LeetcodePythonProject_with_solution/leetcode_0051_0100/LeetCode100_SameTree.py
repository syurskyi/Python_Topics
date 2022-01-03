'''
Created on Jan 31, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        __ n.. p a.. n.. q:
            r.. T..
        ____ n.. p o. n.. q:
            r.. F..
        ____ p.val != q.val:
            r.. F..
        ____:
            r.. isSameTree(p.left, q.left) a..\
                isSameTree(p.right, q.right)