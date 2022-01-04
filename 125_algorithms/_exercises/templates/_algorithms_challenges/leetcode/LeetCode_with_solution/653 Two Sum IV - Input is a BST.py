#!/usr/bin/python3
"""
Given a Binary Search Tree and a target number, return true if there exist two
elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ findTarget(self, root: TreeNode, k: i..) __ bool:
        root = root
        r.. walk(root, k)

    ___ walk(self, node, k):
        __ n.. node:
            r.. F..

        target = k - node.val
        __ find(root, target, node):
            r.. T..

        __ walk(node.left, k) o. walk(node.right, k):
            r.. T..

        r.. F..

    ___ find(self, node, target, existing):
        __ n.. node:
            r.. F..

        __ node.val __ target:
            r.. node != existing

        __ target < node.val:
            r.. find(node.left, target, existing)
        ____:
            r.. find(node.right, target, existing)
