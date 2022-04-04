#!/usr/bin/python3
"""
Given a binary tree with N nodes, each node has a different value from
{1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the
right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from
the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's
value, then preorder-traverse the left child, then preorder-traverse the right
child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of
the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may
return the answer in any order.

If we cannot do so, then return the list [-1].

Example 1:

Input: root = [1,2], voyage = [2,1]
Output: [-1]
Example 2:

Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Example 3:

Input: root = [1,2,3], voyage = [1,2,3]
Output: []

Note:

1 <= N <= 100
"""
____ t___ _______ List


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ -
        ret    # list
        i = 0  # currently scanning index of voyage

    ___ flipMatchVoyage  root: TreeNode, voyage: List[i..]) __ List[i..]:
        """
        match the voyage
        Flip the least number of nodes? There is only one answer
        """
        dfs(root, voyage)
        r.. ret

    ___ dfs  node, voyage
        __ n.. node:
            r..

        __ node.val != voyage[i]:
            ret = [-1]
            r..

        i += 1
        __ node.left a.. node.right a.. node.left.val != voyage[i]:
            # flip left and right
            ret.a..(node.val)
            dfs(node.right, voyage)
            dfs(node.left, voyage)
        ____:
            dfs(node.left, voyage)
            dfs(node.right, voyage)
