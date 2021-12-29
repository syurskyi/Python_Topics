'''
Created on Sep 3, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        __ n.. s and n.. t:
            r.. True
        __ n.. s:
            r.. False
        r.. self.isSameTree(s, t) o.\
            self.isSubtree(s.left, t) o.\
            self.isSubtree(s.right, t)
    
    ___ isSameTree(self, s, t):
        __ n.. s and n.. t:
            r.. True
        __ n.. s o. n.. t:
            r.. False
        __ s.val != t.val:
            r.. False
        r.. self.isSameTree(s.left, t.left) and\
            self.isSameTree(s.right, t.right)
