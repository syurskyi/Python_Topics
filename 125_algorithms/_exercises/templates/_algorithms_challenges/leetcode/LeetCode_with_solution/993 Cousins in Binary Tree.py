#!/usr/bin/python3
"""
In a binary tree, the root node is at depth 0, and children of each depth k node
are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have
different parents.

We are given the root of a binary tree with unique values, and the values x and
y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are
cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""

# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution:
    ___ __init__(self):
        self.pi    # list
        self.depths    # list

    ___ isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        need to know parent and depth
        """
        self.dfs(N.., root, x, 0)
        self.dfs(N.., root, y, 0)
        __ l..(self.pi) != 2:
            r.. False
        r.. self.pi[0] != self.pi[1] a.. self.depths[0] __ self.depths[1]


    ___ dfs(self, pi, node, x, depth):
        __ n.. node:
            r..

        __ node.val __ x:
            self.pi.a..(pi)
            self.depths.a..(depth)
            r..

        self.dfs(node, node.left, x, depth + 1)
        self.dfs(node, node.right, x, depth + 1)
