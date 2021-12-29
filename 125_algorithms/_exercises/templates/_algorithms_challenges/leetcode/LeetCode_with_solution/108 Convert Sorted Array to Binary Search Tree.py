"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution:
    ___ sortedArrayToBST(self, num):
        """
        post-order, dfs
        :param num: list of integers
        :return: TreeNode
        """
        __ n.. num:
            r.. N..

        mid = (0+l..(num))/2
        left_subtree = self.sortedArrayToBST(num[0:mid])
        right_subtree = self.sortedArrayToBST(num[mid+1:])

        root = TreeNode(num[mid])
        root.left = left_subtree
        root.right = right_subtree

        r.. root

