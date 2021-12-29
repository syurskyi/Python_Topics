'''
Created on Feb 22, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ n.. root: r.. N..
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        r.. root
    
    ___ invertTreeNonRec(self, root):
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