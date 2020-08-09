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
    ___ flatten(self, root
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        __ not root: r_ root
        stack = [root]
        prev = TreeNode(-1)
        w___ stack:
            node = stack.pop()
            prev.right = node
            __ node.right:
                stack.append(node.right)
                node.right = None
            __ node.left:
                stack.append(node.left)
                node.left = None
            prev = node
