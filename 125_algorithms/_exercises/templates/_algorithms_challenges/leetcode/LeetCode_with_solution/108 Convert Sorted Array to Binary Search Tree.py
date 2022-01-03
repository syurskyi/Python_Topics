"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution:
    ___ sortedArrayToBST(self, num):
        """
        post-order, dfs
        :param num: list of integers
        :return: TreeNode
        """
        __ n.. num:
            r.. N..

        mid = (0+l..(num))/2
        left_subtree = sortedArrayToBST(num[0:mid])
        right_subtree = sortedArrayToBST(num[mid+1:])

        root = TreeNode(num[mid])
        root.left = left_subtree
        root.right = right_subtree

        r.. root

