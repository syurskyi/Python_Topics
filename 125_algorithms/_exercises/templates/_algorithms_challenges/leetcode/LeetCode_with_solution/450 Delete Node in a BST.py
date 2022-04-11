#!/usr/bin/python3
"""
Given a root node reference of a BST and a key, delete the node with the given
key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Note: Time complexity should be O(height of tree).
"""

# Definition for a binary tree node.
c_ TreeNode:
  ___ - , x
      val x
      left N..
      right N..


c_ Solution:
    ___ deleteNode  root, key
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        r.. _delete(root, key)

    ___ _delete  root, key
        """
        Pop the left max or right min
        Return the root to keep the parent child relationship
        """
        __ n.. root:
            r..

        # check before recursion because need to know parent
        __ key < root.val:
            root.left _delete(root.left, key)
            r.. root
        ____ key > root.val:
            root.right _delete(root.right, key)
            r.. root
        ____
            __ root.left:
                maxa, left _pop_max(root.left)
                root.left left
                root.val maxa
                r.. root
            ____ root.right:
                mini, right _pop_min(root.right)
                root.right right
                root.val mini
                r.. root
            ____
                r..

    ___ _pop_max  root
        __ root.right:
            maxa, right _pop_max(root.right)
            root.right right
            r.. maxa, root
        # irrevelant with root.left, BST property
        ____
            r.. root.val, root.left

    ___ _pop_min  root
        __ root.left:
            mini, left _pop_min(root.left)
            root.left left
            r.. mini, root
        # irrevelant with root.right, BST property
        ____
            r.. root.val, root.right

    ___ _delete_error  root, key
        """
        need to know the parent, keep the reference
        need to handle duplicate

        Error: need to find the max of the left subtree rather than the root
        """
        __ n.. root:
            r..

        # check before recursion because need to know parent
        __ key < root.val:
            root.left _delete(root.left, key)
            r.. root
        ____ key > root.val:
            root.right _delete(root.right, key)
            r.. root
        ____
            __ root.left:
                root.val root.left.val
                left _delete(root.left, root.left.val)
                root.left left
                r.. root
            ____ root.right:
                root.val root.right.val
                right _delete(root.right, root.right.val)
                root.right right
                r.. root
            ____
                r..
