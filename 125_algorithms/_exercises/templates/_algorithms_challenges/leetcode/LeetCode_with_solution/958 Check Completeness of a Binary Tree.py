#!/usr/bin/python3
"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely
filled, and all nodes in the last level are as far left as possible. It can have
between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values
{1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:

Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ -
        max_depth -f__("inf")
        expecting_partial F..

    ___ isCompleteTree  root: TreeNode) __ b..
        """
        Do it in one pass
        Left first dfs
        Record the max depth and expecting partial fill in the last level
        Need a special flag to tell whether expecting partial now
        """
        r.. dfs(root, 0)

    ___ dfs  node, d
        __ n.. node:
            # empty node (below leaf) is the key decision point
            __ max_depth __ -f__("inf"  # leftmost empty node
                max_depth d - 1
                r.. T..
            ____ expecting_partial:
                r.. d __ max_depth
            ____
                __ d __ max_depth + 1:
                    r.. T..
                __ d __ max_depth:
                    expecting_partial T..
                    r.. T..
                r.. F..

        r.. dfs(node.left, d + 1) a.. dfs(node.right, d + 1)
