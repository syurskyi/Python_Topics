# -*- coding: utf-8 -*-
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:
"""
__author__ = 'Daniel'


c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ kthSmallest  root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = cnt(root.left)
        __ l+1 __ k:
            r.. root.val
        ____ l+1 < k:
            r.. kthSmallest(root.right, k-(l+1))
        ____:
            r.. kthSmallest(root.left, k)

    ___ cnt  root):
        __ n.. root:
            r.. 0

        r.. 1+cnt(root.left)+cnt(root.right)