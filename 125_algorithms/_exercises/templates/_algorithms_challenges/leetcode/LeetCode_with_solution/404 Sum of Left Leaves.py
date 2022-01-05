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
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution(object):
    ___ - ):
        s = 0

    ___ sumOfLeftLeaves  root):
        """
        :type root: TreeNode
        :rtype: int
        """
        traverse(root)
        r.. s

    ___ traverse  node):
        __ n.. node:
            r..

        __ node.left a.. n.. node.left.left a.. n.. node.left.right:
            s += node.left.val

        traverse(node.left)
        traverse(node.right)
