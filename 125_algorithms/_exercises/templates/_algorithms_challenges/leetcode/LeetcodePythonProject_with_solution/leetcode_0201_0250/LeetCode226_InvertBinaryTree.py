'''
Created on Feb 22, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ invertTree  root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root: r.. N..
        left = invertTree(root.left)
        right = invertTree(root.right)
        root.left = right
        root.right = left
        r.. root
    
    ___ invertTreeNonRec  root):
        __ n.. root: r.. N..
        stack = [root]
        w.... stack:
            node = stack.pop()
            __ node:
                left = node.left
                right = node.right
                node.right = left
                node.left = right
                stack.a..(left)
                stack.a..(right)
        r.. root