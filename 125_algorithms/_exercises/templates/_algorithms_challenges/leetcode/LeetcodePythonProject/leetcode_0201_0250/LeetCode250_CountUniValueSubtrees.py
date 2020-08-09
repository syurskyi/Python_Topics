'''
Created on May 13, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ countUnivalSubtrees(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        __ not root: r_ res
        __ self.isUniVal(root
            res += 1
        res += self.countUnivalSubtrees(root.left)+\
            self.countUnivalSubtrees(root.right)
        r_ res
    
    ___ isUniVal(self, root
        __ not root.left and not root.right:
            r_ True
        __ not root.right:
            r_ root.val __ root.left.val and self.isUniVal(root.left)
        __ not root.left:
            r_ root.val __ root.right.val and self.isUniVal(root.right)
        r_ root.left.val __ root.val and root.right.val __ root.val and\
            self.isUniVal(root.left) and self.isUniVal(root.right)
