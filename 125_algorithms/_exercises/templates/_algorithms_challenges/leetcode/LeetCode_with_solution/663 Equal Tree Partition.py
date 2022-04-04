#!/usr/bin/python3
"""
premium question
"""

# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ -
        sums    # list

    ___ checkEqualTree  root: TreeNode) __ b..:
        """
        To save 2nd pass, store sums
        space: O(N)
        """
        dfs(root)
        total = sums.p.. )
        r.. total % 2 __ 0 a.. total // 2 __ sums

    ___ dfs  node
        __ n.. node:
            r.. 0

        l = dfs(node.left)
        r = dfs(node.right)
        s = l + r + node.val
        sums.a..(s)
        r.. s


c_ Solution:
    ___ -
        """
        Save space, two passes
        """
        exists = F..
        root = N..  # need to handle 0
        total_sum = N..

    ___ checkEqualTree  root: TreeNode) __ b..:
        """
        two passes
        1st pass, get total sum
        2nd pass, check whether has sum/2
        space: O(log N)

        To save 2nd pass, store sums
        space: O(N)
        """
        root = root
        total_sum = dfs(root)
        dfs(root)
        r.. exists

    ___ dfs  node
        __ n.. node:
            r.. 0

        l = dfs(node.left)
        r = dfs(node.right)
        s = l + r + node.val
        __ node != root a.. total_sum != N.. a.. total_sum __ s * 2:
            exists = T..

        r.. s
