'''
Created on May 13, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        __ not root: return res
        __ self.isUniVal(root):
            res += 1
        res += self.countUnivalSubtrees(root.left)+\
            self.countUnivalSubtrees(root.right)
        return res
    
    ___ isUniVal(self, root):
        __ not root.left and not root.right:
            return True
        __ not root.right:
            return root.val == root.left.val and self.isUniVal(root.left)
        __ not root.left:
            return root.val == root.right.val and self.isUniVal(root.right)
        return root.left.val == root.val and root.right.val == root.val and\
            self.isUniVal(root.left) and self.isUniVal(root.right)
