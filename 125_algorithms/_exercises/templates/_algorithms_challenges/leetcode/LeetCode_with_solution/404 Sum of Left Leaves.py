"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
__author__ = 'Daniel'


# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ __init__(self):
        self.s = 0

    ___ sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        r.. self.s

    ___ traverse(self, node):
        __ n.. node:
            r..

        __ node.left and n.. node.left.left and n.. node.left.right:
            self.s += node.left.val

        self.traverse(node.left)
        self.traverse(node.right)
