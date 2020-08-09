'''
Created on Jan 31, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ isSameTree(self, p, q
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        __ not p and not q:
            r_ True
        ____ not p or not q:
            r_ False
        ____ p.val != q.val:
            r_ False
        ____
            r_ self.isSameTree(p.left, q.left) and\
                self.isSameTree(p.right, q.right)