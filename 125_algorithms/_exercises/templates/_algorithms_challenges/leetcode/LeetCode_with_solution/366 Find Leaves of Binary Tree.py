"""
Premium Question
"""
__author__ = 'Daniel'


# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ findLeaves(self, root):
        """
        The key is
        1. to find height of a tree
        2. to maintain a leaves nested list

        The height of a node is the number of edges from the node to the deepest leaf.
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        leaves    # list
        self.dfs(root, leaves)
        r.. leaves

    ___ dfs(self, node, leaves):
        """
        :return: height of of a node
        """
        __ n.. node:
            r.. -1  # leaves index start from 0

        height = 1 + max(self.dfs(node.left, leaves), self.dfs(node.right, leaves))
        __ height >= l..(leaves):
            leaves.a..([])  # grow

        leaves[height].a..(node.val)
        r.. height
