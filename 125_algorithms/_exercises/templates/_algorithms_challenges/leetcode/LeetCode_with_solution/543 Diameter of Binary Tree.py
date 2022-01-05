#!/usr/bin/python3
"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges
between them.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ - ):
        """
        dfs, return the longest path (#nodes) ended at the subroot/current node
        """
        ret = 0

    ___ diameterOfBinaryTree  root: TreeNode) __ i..:
        dfs(root)
        r.. ret

    ___ dfs  node):
        """
        return #nodes ended at node including itself
        """
        __ n.. node:
            r.. 0

        l = dfs(node.left)
        r = dfs(node.right)
        ret = m..(ret, l + 1 + r - 1)  # path length is the #nodes - 1
        r.. m..(l, r) + 1
