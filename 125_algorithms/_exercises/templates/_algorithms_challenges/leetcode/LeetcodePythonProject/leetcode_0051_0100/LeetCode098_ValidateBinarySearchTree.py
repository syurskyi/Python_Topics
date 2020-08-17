'''
Created on Jan 30, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution(object
    ___ isValidBST(self, root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ not root: r_ True
        stack = []
        prev = float('-inf')
        node = root
        w___ node:
            stack.append(node)
            node = node.left
        w___ stack:
            node = stack.p..
            __ prev >= node.val:
                r_ False
            prev = node.val
            node0 = node.right
            w___ node0:
                stack.append(node0)
                node0 = node0.left
        r_ True
