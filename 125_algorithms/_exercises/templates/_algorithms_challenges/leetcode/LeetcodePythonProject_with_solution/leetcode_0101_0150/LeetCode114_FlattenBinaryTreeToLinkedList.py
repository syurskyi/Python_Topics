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
    ___ flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        __ n.. root: r.. root
        stack = [root]
        prev = TreeNode(-1)
        w.... stack:
            node = stack.pop()
            prev.right = node
            __ node.right:
                stack.a..(node.right)
                node.right = N..
            __ node.left:
                stack.a..(node.left)
                node.left = N..
            prev = node
