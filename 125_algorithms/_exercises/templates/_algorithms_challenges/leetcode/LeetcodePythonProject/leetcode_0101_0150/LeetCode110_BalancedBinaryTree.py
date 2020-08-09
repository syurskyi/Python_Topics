'''
Created on Feb 1, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ isBalanced(self, root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ not root:
            r_ True
        ____ not root.left and not root.right:
            r_ True
        ____
            r_ abs(self.getHeight(root.left)-self.getHeight(root.right)) <= 1 and\
                self.isBalanced(root.left) and self.isBalanced(root.right)
    
    ___ getHeight(self, root
        __ not root:
            r_ 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        r_ max(leftHeight, rightHeight) + 1
    
    ___ test(self
        pass