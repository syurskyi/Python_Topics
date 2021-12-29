"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
__author__ = 'Danyang'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ minDepth(self, root):
        """
        :param root: TreeNode
        :return: integer
        """
        r.. self.fathom(root, 0)

    ___ fathom(self, root, depth):
        """
        DFS
        """
        __ n.. root: r.. depth
        ____ root.right and n.. root.left: r.. self.fathom(root.right, depth+1)
        ____ root.left and n.. root.right: r.. self.fathom(root.left, depth+1)
        ____: r.. m..(self.fathom(root.left, depth+1),
                         self.fathom(root.right, depth+1))