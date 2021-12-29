'''
Created on May 13, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
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
        __ n.. root: r.. res
        __ self.isUniVal(root):
            res += 1
        res += self.countUnivalSubtrees(root.left)+\
            self.countUnivalSubtrees(root.right)
        r.. res
    
    ___ isUniVal(self, root):
        __ n.. root.left a.. n.. root.right:
            r.. True
        __ n.. root.right:
            r.. root.val __ root.left.val a.. self.isUniVal(root.left)
        __ n.. root.left:
            r.. root.val __ root.right.val a.. self.isUniVal(root.right)
        r.. root.left.val __ root.val a.. root.right.val __ root.val a..\
            self.isUniVal(root.left) a.. self.isUniVal(root.right)
