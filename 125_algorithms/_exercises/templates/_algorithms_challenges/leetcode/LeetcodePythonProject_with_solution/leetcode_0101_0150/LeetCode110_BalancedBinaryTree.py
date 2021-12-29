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
    ___ isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root:
            r.. True
        ____ n.. root.left and n.. root.right:
            r.. True
        ____:
            r.. abs(self.getHeight(root.left)-self.getHeight(root.right)) <= 1 and\
                self.isBalanced(root.left) and self.isBalanced(root.right)
    
    ___ getHeight(self, root):
        __ n.. root:
            r.. 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        r.. max(leftHeight, rightHeight) + 1
    
    ___ test(self):
        pass