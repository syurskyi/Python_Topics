"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
__author__ = 'Danyang'


c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution(o..
    ___ minDepth  root
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
        ____ root.right a.. n.. root.left: r.. fathom(root.right, depth+1)
        ____ root.left a.. n.. root.right: r.. fathom(root.left, depth+1)
        ____ r.. m..(fathom(root.left, depth+1),
                         fathom(root.right, depth+1