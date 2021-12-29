'''
Created on Jan 30, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution(object):
    ___ isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ n.. root: r.. True
        stack    # list
        prev = float('-inf')
        node = root
        w.... node:
            stack.a..(node)
            node = node.left
        w.... stack:
            node = stack.pop()
            __ prev >= node.val:
                r.. False
            prev = node.val
            node0 = node.right
            w.... node0:
                stack.a..(node0)
                node0 = node0.left
        r.. True
