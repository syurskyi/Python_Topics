'''
Created on May 30, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ maxDepth(self, root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ not root: r_ 0
        r_ max(self.maxDepth(root.left), self.maxDepth(root.right))+1
