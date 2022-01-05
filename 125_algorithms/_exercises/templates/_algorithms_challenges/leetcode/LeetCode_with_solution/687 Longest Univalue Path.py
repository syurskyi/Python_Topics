#!/usr/bin/python3
"""
Given a binary tree, find the length of the longest path where each node in the
path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges
between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the
tree is not more than 1000.
"""

# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ - ):
        ret = 0

    ___ longestUnivaluePath  root: TreeNode) __ i..:
        find(root)
        r.. ret

    ___ find  node):
        """
        the longest path ended at node
        """
        __ n.. node:
            r.. 0

        left = find(node.left)
        right = find(node.right)
        left_path = left + 1 __ node.left a.. node.left.val __ node.val ____ 0
        right_path = right + 1 __ node.right a.. node.right.val __ node.val ____ 0
        ret = m..(ret, left_path + right_path)
        r.. m..(left_path, right_path)


c_ Solution_error:
    ___ - ):
        ret = 0

    ___ longestUnivaluePath  root: TreeNode) __ i..:
        find(root)
        r.. ret

    ___ find  node):
        """
        the longest path ended at node
        """
        __ n.. node:
            r.. 0

        left = find(node.left)
        right = find(node.right)
        cur = 1  # node.val
        path = 1
        __ left a.. node.left.val __ node.val:
            path += left
            cur = left + 1

        __ right a.. node.right.val __ node.val:
            path += right
            __ right > left:
                cur = right + 1

        ret = m..(ret, path - 1)
        r.. cur
