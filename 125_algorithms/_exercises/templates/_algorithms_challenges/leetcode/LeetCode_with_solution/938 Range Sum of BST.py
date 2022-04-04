#!/usr/bin/python3
"""
Given the root node of a binary search tree, return the sum of values of all
nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ -
        ret = 0

    ___ rangeSumBST  root: TreeNode, L: i.., R: i..) __ i..:
        """
        traverse
        """
        dfs(root, L, R)
        r.. ret

    ___ dfs  node, L, R
        __ n.. node:
            r..

        __ L <_ node.val <_ R:
            ret += node.val
            dfs(node.left, L, R)
            dfs(node.right, L, R)

        ____ node.val > R:
            dfs(node.left, L, R)
        ____
            dfs(node.right, L, R)
