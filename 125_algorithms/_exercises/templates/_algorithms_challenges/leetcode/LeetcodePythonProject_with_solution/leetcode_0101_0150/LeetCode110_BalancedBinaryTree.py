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
    ___ isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root:
            r.. T..
        ____ n.. root.left a.. n.. root.right:
            r.. T..
        ____:
            r.. abs(getHeight(root.left)-getHeight(root.right)) <= 1 a..\
                isBalanced(root.left) a.. isBalanced(root.right)
    
    ___ getHeight(self, root):
        __ n.. root:
            r.. 0
        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)
        r.. max(leftHeight, rightHeight) + 1
    
    ___ test
        pass