#!/usr/bin/python3
"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ findBottomLeftValue  root):
        """
        BFS

        :type root: TreeNode
        :rtype: int
        """
        q = [root]
        w.... q:
            ret = q[0].val
            cur_q    # list
            ___ e __ q:
                __ e.left:
                    cur_q.a..(e.left)
                __ e.right:
                    cur_q.a..(e.right)
            q = cur_q

        r.. ret
