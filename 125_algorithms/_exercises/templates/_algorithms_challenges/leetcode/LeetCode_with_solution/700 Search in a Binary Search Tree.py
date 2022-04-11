#!/usr/bin/python3
"""
Given the root node of a binary search tree (BST) and a value. You need to
find the node in the BST that the node's value equals the given value. Return
the subtree rooted with that node. If such node doesn't exist, you should return
NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node
with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the
expected output (serialized tree format) as [], not null.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ searchBST  root: TreeNode, val: i..) __ TreeNode:
        __ n.. root:
            r.. N..

        __ root.val __ val:
            r.. root
        ____ root.val < val:
            r.. searchBST(root.right, val)
        ____
            r.. searchBST(root.left, val)
