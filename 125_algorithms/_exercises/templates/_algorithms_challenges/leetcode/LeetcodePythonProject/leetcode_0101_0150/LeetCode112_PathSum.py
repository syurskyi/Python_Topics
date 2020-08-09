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
    ___ hasPathSum(self, root, sumVal
        """
        :type root: TreeNode
        :type sumVal: int
        :rtype: bool
        """
        __ not root:
            r_ False
        __ root.val __ sumVal and not root.left and not root.right:
            r_ True
        ____
            r_ self.hasPathSum(root.left, sumVal-root.val) or\
                self.hasPathSum(root.right, sumVal-root.val)
    