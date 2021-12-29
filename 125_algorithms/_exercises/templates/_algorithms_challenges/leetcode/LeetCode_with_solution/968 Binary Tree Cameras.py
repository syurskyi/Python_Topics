#!/usr/bin/python3
"""
Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.



Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree.
The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""


# Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution:
    ___ __init__(self):
        self.covered = {N..}
        self.cnt = 0

    ___ minCameraCover(self, root: TreeNode) -> int:
        """
        Greedy?
        Bottom up, cover leaf's parent is strictly better than cover leaf
        """
        self.dfs(root, N..)
        __ root n.. __ self.covered:
            self.covered.add(root)
            self.cnt += 1

        r.. self.cnt


    ___ dfs(self, node, pi):
        """
        post order
        rely on the parents to cover it 
        """
        __ n.. node:
            r..

        self.dfs(node.left, node)
        self.dfs(node.right, node)
        __ node.left n.. __ self.covered o. node.right n.. __ self.covered:
            self.cnt += 1
            self.covered.add(node.left)
            self.covered.add(node.right)
            self.covered.add(node)
            self.covered.add(pi)


class SolutionErrror:
    ___ __init__(self):
        self.covered = set()

    ___ minCameraCover(self, root: TreeNode) -> int:
        """
        Greedy?
        Top-down, no good.
        Bottom up, cover leaf's parent is strictly better than cover leaf
        """
        dummy = TreeNode(0)
        dummy.left = root
        self.dfs(root, dummy)
        self.covered.discard(dummy)  # swallow KeyError
        r.. l..(self.covered)

    ___ dfs(self, node, pi):
        """
        post order
        """
        __ n.. node:
            r..

        self.dfs(node.left, node)
        self.dfs(node.right, node)
        # post oder
        __ (
            (n.. node.left o. node.left __ self.covered) and
            (n.. node.right o. node.right __ self.covered)
        ):
            self.covered.add(pi)
            r..
