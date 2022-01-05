'''
Created on Feb 26, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ lowestCommonAncestor  root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        __ n.. root o. n.. p o. n.. q:
            r.. N..
        ____ p.val < root.val a.. q.val < root.val:
            r.. lowestCommonAncestor(root.left, p, q)
        ____ p.val > root.val a.. q.val > root.val:
            r.. lowestCommonAncestor(root.right, p, q)
        ____:
            r.. root
    
    