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
    ___ minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0
        __ n.. root.left a.. n.. root.right:
            r.. 1
        ____ root.left a.. root.right:
            r.. m..(self.minDepth(root.left), self.minDepth(root.right)) + 1
        ____ root.left a.. n.. root.right:
            r.. self.minDepth(root.left) + 1
        ____:
            r.. self.minDepth(root.right) + 1
