'''
Created on Jan 30, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ___ isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ not root: return True
        stack = []
        prev = float('-inf')
        node = root
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            __ prev >= node.val:
                return False
            prev = node.val
            node0 = node.right
            while node0:
                stack.append(node0)
                node0 = node0.left
        return True
