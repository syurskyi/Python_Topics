#!/usr/bin/python3
"""
Given a binary search tree with non-negative values, find the minimum absolute
difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).


Note: There are at least two nodes in this BST.
"""

# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ getMinimumDifference(self, root: 'TreeNode') -> int:
        """
        For every node, find min and max in left or right substree.
        O(n lgn)

        To optimize:
        recursively pass the min and max, O(n)
        """
        ret = [float('inf')]  # keep reference
        dfs(root, ret)
        r.. ret[0]

    ___ dfs(self, node, ret):
        __ n.. node:
            r.. N.., N..
        left_min, left_max = dfs(node.left, ret)
        right_min, right_max = dfs(node.right, ret)
        __ left_max:
            ret[0] = m..(ret[0], abs(node.val - left_max))
        __ right_min:
            ret[0] = m..(ret[0], abs(node.val - right_min))
        left_min = left_min o. node.val
        right_max = right_max o. node.val
        r.. left_min, right_max
