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
class TreeNode:
  ___ __init__(self, x
      self.val = x
      self.left = None
      self.right = None


class Solution:
    ___ deleteNode(self, root, key
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        r_ self._delete(root, key)

    ___ _delete(self, root, key
        """
        Pop the left max or right min
        Return the root to keep the parent child relationship
        """
        __ not root:
            r_

        # check before recursion because need to know parent
        __ key < root.val:
            root.left = self._delete(root.left, key)
            r_ root
        ____ key > root.val:
            root.right = self._delete(root.right, key)
            r_ root
        ____
            __ root.left:
                maxa, left = self._pop_max(root.left)
                root.left = left
                root.val = maxa
                r_ root
            ____ root.right:
                mini, right = self._pop_min(root.right)
                root.right = right
                root.val = mini
                r_ root
            ____
                r_

    ___ _pop_max(self, root
        __ root.right:
            maxa, right = self._pop_max(root.right)
            root.right = right
            r_ maxa, root
        # irrevelant with root.left, BST property
        ____
            r_ root.val, root.left

    ___ _pop_min(self, root
        __ root.left:
            mini, left = self._pop_min(root.left)
            root.left = left
            r_ mini, root
        # irrevelant with root.right, BST property
        ____
            r_ root.val, root.right

    ___ _delete_error(self, root, key
        """
        need to know the parent, keep the reference
        need to handle duplicate

        Error: need to find the max of the left subtree rather than the root
        """
        __ not root:
            r_

        # check before recursion because need to know parent
        __ key < root.val:
            root.left = self._delete(root.left, key)
            r_ root
        ____ key > root.val:
            root.right = self._delete(root.right, key)
            r_ root
        ____
            __ root.left:
                root.val = root.left.val
                left = self._delete(root.left, root.left.val)
                root.left = left
                r_ root
            ____ root.right:
                root.val = root.right.val
                right = self._delete(root.right, root.right.val)
                root.right = right
                r_ root
            ____
                r_
