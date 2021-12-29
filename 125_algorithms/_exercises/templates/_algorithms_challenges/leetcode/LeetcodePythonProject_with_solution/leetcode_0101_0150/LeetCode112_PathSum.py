'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ hasPathSum(self, root, sumVal):
        """
        :type root: TreeNode
        :type sumVal: int
        :rtype: bool
        """
        __ n.. root:
            r.. False
        __ root.val __ sumVal a.. n.. root.left a.. n.. root.right:
            r.. True
        ____:
            r.. self.hasPathSum(root.left, sumVal-root.val) o.\
                self.hasPathSum(root.right, sumVal-root.val)
    