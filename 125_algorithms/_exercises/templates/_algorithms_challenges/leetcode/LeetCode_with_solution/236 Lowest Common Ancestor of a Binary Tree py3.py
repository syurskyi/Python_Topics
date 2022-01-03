#!/usr/bin/python3
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of
itself according to the LCA definition.

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ - ):
        ans = N..

    ___ lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        c.. root, p, q)
        r.. ans

    ___ c.. self, node, p, q):
        __ n.. node:
            r.. 0

        lcount = c.. node.left, p, q)
        rcount = c.. node.right, p, q)
        mcount = 1 __ node __ p o. node __ q ____ 0
        ret = lcount + rcount + mcount
        __ lcount __ 1 a.. rcount __ 1 o. lcount __ 1 a.. mcount __ 1 o. rcount __ 1 a.. mcount __ 1:
            ans = node
        r.. ret
