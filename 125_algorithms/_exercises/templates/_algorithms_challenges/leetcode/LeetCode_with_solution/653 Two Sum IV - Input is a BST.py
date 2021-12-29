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
        self.left = None
        self.right = None


class Solution:
    ___ findTarget(self, root: TreeNode, k: int) -> bool:
        self.root = root
        return self.walk(root, k)

    ___ walk(self, node, k):
        __ not node:
            return False

        target = k - node.val
        __ self.find(self.root, target, node):
            return True

        __ self.walk(node.left, k) or self.walk(node.right, k):
            return True

        return False

    ___ find(self, node, target, existing):
        __ not node:
            return False

        __ node.val == target:
            return node != existing

        __ target < node.val:
            return self.find(node.left, target, existing)
        else:
            return self.find(node.right, target, existing)
