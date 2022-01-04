#!/usr/bin/python3
"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every
key of the original BST is changed to the original key plus sum of all keys
greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ convertBST(self, root: 'TreeNode') __ 'TreeNode':
        """
        in-order traversal, right first
        """
        walk(root, 0)
        r.. root

    ___ walk(self, node, cur_sum):
        """stateless walk"""
        __ n.. node:
            r.. cur_sum
        s = walk(node.right, cur_sum)
        node.val += s
        r.. walk(node.left, node.val)
