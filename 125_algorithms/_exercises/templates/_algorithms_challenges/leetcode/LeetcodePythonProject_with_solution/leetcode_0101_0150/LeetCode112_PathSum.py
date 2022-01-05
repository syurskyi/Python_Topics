'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(o..):
    ___ hasPathSum  root, sumVal):
        """
        :type root: TreeNode
        :type sumVal: int
        :rtype: bool
        """
        __ n.. root:
            r.. F..
        __ root.val __ sumVal a.. n.. root.left a.. n.. root.right:
            r.. T..
        ____:
            r.. hasPathSum(root.left, sumVal-root.val) o.\
                hasPathSum(root.right, sumVal-root.val)
    