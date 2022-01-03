"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution:
    ___ isValidBST(self, root):
        """
        Google Phone Interview Question, 20 Sep 2013
        recursive dfs

        alternative answer: convert the tree the array and judge whether it is sorted
        :param root: a tree node
        :return: boolean
        """
        __ n.. root:
            r.. T..

        __ n.. isValidBST(root.left):
            r.. F..
        __ n.. isValidBST(root.right):
            r.. F..

        __ root.left:
            __ n.. get_largest(root.left) < root.val:
                r.. F..
        __ root.right:
            __ n.. root.val < get_smallest(root.right):
                r.. F..


        r.. T..

    ___ get_largest(self, root):
        """
        possible dp
        :param root: TreeNode
        :return: integer
        """
        __ n.. root.right:
            r.. root.val
        r.. get_largest(root.right)

    ___ get_smallest(self, root):
        """
        possible dp
        :param root: TreeNode
        :return: integer
        """
        __ n.. root.left:
            r.. root.val
        r.. get_smallest(root.left)



