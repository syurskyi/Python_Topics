#!/usr/bin/python3
"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path
represents a binary number starting with the most significant bit.  For example,
if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary,
which is 13.

For all leaves in the tree, consider the numbers represented by the path from
the root to that leaf.

Return the sum of these numbers.

Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Note:
The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
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
        lst    # list

    ___ sumRootToLeaf  root: TreeNode) __ i..:
        """
        Brute force, keep a lst, space O(log n)
        Error-prone
        """
        dfs(root)
        r.. ret

    ___ dfs  node
        __ n.. node:
            r..

        lst.a..(node.val)  # error prone
        __ n.. node.left a.. n.. node.right:
            # leaf
            cur = 0
            ___ a __ lst:
                cur <<= 1
                cur += a
            ret += cur
        ____:
            dfs(node.left)
            dfs(node.right)
        lst.pop()
