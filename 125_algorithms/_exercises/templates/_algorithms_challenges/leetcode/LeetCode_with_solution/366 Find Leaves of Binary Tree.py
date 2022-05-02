"""
Premium Question
"""
__author__ 'Daniel'


# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x
        val x
        left N..
        right N..


c_ Solution(o..
    ___ findLeaves  root
        """
        The key is
        1. to find height of a tree
        2. to maintain a leaves nested list

        The height of a node is the number of edges from the node to the deepest leaf.
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        leaves    # list
        dfs(root, leaves)
        r.. leaves

    ___ dfs  node, leaves
        """
        :return: height of of a node
        """
        __ n.. node:
            r.. -1  # leaves index start from 0

        height 1 + m..(dfs(node.left, leaves), dfs(node.right, leaves
        __ height >_ l..(leaves
            leaves.a..(   # list)  # grow

        leaves[height].a..(node.val)
        r.. height
