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


class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution:
    ___ kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = self.cnt(root.left)
        __ l+1 __ k:
            r.. root.val
        ____ l+1 < k:
            r.. self.kthSmallest(root.right, k-(l+1))
        ____:
            r.. self.kthSmallest(root.left, k)

    ___ cnt(self, root):
        __ n.. root:
            r.. 0

        r.. 1+self.cnt(root.left)+self.cnt(root.right)