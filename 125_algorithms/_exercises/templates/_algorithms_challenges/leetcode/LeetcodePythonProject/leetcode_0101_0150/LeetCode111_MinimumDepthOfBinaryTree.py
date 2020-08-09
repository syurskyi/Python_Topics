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
    ___ minDepth(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root:
            r_ 0
        __ not root.left and not root.right:
            r_ 1
        ____ root.left and root.right:
            r_ min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        ____ root.left and not root.right:
            r_ self.minDepth(root.left) + 1
        ____
            r_ self.minDepth(root.right) + 1
