'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..

c_ Solution(o..
    ___ isBalanced  root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root:
            r.. T..
        ____ n.. root.left a.. n.. root.right:
            r.. T..
        ____
            r.. abs(getHeight(root.left)-getHeight(root.right <= 1 a..\
                isBalanced(root.left) a.. isBalanced(root.right)
    
    ___ getHeight  root
        __ n.. root:
            r.. 0
        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)
        r.. m..(leftHeight, rightHeight) + 1
    
    ___ test
        p..