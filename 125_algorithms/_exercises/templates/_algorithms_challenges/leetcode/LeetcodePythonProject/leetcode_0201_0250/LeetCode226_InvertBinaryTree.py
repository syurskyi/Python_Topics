'''
Created on Feb 22, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ invertTree(self, root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        __ not root: r_ None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        r_ root
    
    ___ invertTreeNonRec(self, root
        __ not root: r_ None
        stack = [root]
        w___ stack:
            node = stack.p..
            __ node:
                left = node.left
                right = node.right
                node.right = left
                node.left = right
                stack.append(left)
                stack.append(right)
        r_ root