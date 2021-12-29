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
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution:
    ___ findTarget(self, root: TreeNode, k: int) -> bool:
        self.root = root
        r.. self.walk(root, k)

    ___ walk(self, node, k):
        __ n.. node:
            r.. False

        target = k - node.val
        __ self.find(self.root, target, node):
            r.. True

        __ self.walk(node.left, k) o. self.walk(node.right, k):
            r.. True

        r.. False

    ___ find(self, node, target, existing):
        __ n.. node:
            r.. False

        __ node.val __ target:
            r.. node != existing

        __ target < node.val:
            r.. self.find(node.left, target, existing)
        ____:
            r.. self.find(node.right, target, existing)
