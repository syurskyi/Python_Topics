'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root: r.. 0
        r.. max(maxDepth(root.left), maxDepth(root.right))+1
