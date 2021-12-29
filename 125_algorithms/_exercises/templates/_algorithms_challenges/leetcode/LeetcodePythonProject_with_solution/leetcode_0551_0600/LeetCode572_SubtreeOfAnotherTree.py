'''
Created on Sep 3, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        __ not s and not t:
            return True
        __ not s:
            return False
        return self.isSameTree(s, t) or\
            self.isSubtree(s.left, t) or\
            self.isSubtree(s.right, t)
    
    ___ isSameTree(self, s, t):
        __ not s and not t:
            return True
        __ not s or not t:
            return False
        __ s.val != t.val:
            return False
        return self.isSameTree(s.left, t.left) and\
            self.isSameTree(s.right, t.right)
