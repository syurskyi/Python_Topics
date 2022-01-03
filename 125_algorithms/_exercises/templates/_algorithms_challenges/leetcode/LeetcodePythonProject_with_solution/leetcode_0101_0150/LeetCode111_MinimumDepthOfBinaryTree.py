'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
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
            r.. m..(minDepth(root.left), minDepth(root.right)) + 1
        ____ root.left a.. n.. root.right:
            r.. minDepth(root.left) + 1
        ____:
            r.. minDepth(root.right) + 1
