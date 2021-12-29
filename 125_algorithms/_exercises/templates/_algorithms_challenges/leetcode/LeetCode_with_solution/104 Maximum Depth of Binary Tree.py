"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
__author__ = 'Danyang'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # @param root, a tree node
    # @return an integer
    ___ maxDepth(self, root):
        """
        :param root: TreeNode
        :return: integer
        """
        return self.fathom(root, 0)

    ___ fathom(self, root, depth):
        """
        DFS
        """
        __ not root: return depth
        else: return max(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))
