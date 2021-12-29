'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root: r.. 0
        r.. max(self.maxDepth(root.left), self.maxDepth(root.right))+1
