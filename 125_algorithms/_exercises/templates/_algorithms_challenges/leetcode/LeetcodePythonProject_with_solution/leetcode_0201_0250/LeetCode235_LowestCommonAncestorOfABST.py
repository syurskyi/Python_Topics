'''
Created on Feb 26, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        __ n.. root o. n.. p o. n.. q:
            r.. N..
        ____ p.val < root.val and q.val < root.val:
            r.. self.lowestCommonAncestor(root.left, p, q)
        ____ p.val > root.val and q.val > root.val:
            r.. self.lowestCommonAncestor(root.right, p, q)
        ____:
            r.. root
    
    