#!/usr/bin/python3
"""
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L). You might need
to change the root of the tree, so the result should return the new root of the
trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ trimBST  root: TreeNode, L: i.., R: i..) __ TreeNode:
        """
        post-order traverse
        """
        r.. walk(root, L, R)

    ___ walk  node, L, R
        __ n.. node:
            r.. N..

        node.left = walk(node.left, L, R)
        node.right = walk(node.right, L, R)
        __ node.val < L:
            r.. node.right
        ____ node.val > R:
            r.. node.left
        ____:
            r.. node
