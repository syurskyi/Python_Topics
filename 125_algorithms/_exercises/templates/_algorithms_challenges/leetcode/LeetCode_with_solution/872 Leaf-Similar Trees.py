#!/usr/bin/python3
"""
Consider all the leaves of a binary tree.  From left to right order, the values
of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
8).

Two binary trees are considered leaf-similar if their leaf value sequence is the
same.

Return true if and only if the two given trees with head nodes root1 and root2
are leaf-similar.

Note:

Both of the given trees will have between 1 and 100 nodes.
"""

# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ leafSimilar  root1: TreeNode, root2: TreeNode) __ bool:
        """
        brute force, get all the leaf and then compare
        to save space, use generator
        O(lg n) space for the stack
        """
        itr1 = dfs(root1)
        itr2 = dfs(root2)
        w... T...
            a = next(itr1, N..)
            b = next(itr2, N..)
            __ a != b:
                r.. F..
            __ a __ N.. a.. b __ N..
                _____
        r.. T..

    ___ dfs  node):
        stk = [node]
        # pre-order
        w.... stk:
            cur = stk.pop()
            __ n.. cur:
                _____
            __ n.. cur.left a.. n.. cur.right:
                y.. cur.val
            ____:
                stk.a..(cur.right)
                stk.a..(cur.left)
