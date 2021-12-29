#!/usr/bin/python3
"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.



Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false


Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
"""

# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution:
    ___ isUnivalTree(self, root: TreeNode) -> bool:
        r.. self.dfs(root, root.val __ root ____ N..)

    ___ dfs(self, node, val) -> bool:
        __ n.. node:
            r.. True
        __ node.val != val:
            r.. False

        r.. self.dfs(node.left, val) and self.dfs(node.right, val)
