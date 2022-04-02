"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
__author__ = 'Danyang'


c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution(o..
    # @param root, a tree node
    # @return an integer
    ___ maxDepth  root
        """
        :param root: TreeNode
        :return: integer
        """
        r.. fathom(root, 0)

    ___ fathom  root, depth
        """
        DFS
        """
        __ n.. root: r.. depth
        ____: r.. m..(fathom(root.left, depth+1), fathom(root.right, depth+1))
