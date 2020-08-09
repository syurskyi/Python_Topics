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
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ___ isValidBST(self, root
        """
        Google Phone Interview Question, 20 Sep 2013
        recursive dfs

        alternative answer: convert the tree the array and judge whether it is sorted
        :param root: a tree node
        :return: boolean
        """
        __ not root:
            r_ True

        __ not self.isValidBST(root.left
            r_ False
        __ not self.isValidBST(root.right
            r_ False

        __ root.left:
            __ not self.get_largest(root.left) < root.val:
                r_ False
        __ root.right:
            __ not root.val < self.get_smallest(root.right
                r_ False


        r_ True

    ___ get_largest(self, root
        """
        possible dp
        :param root: TreeNode
        :return: integer
        """
        __ not root.right:
            r_ root.val
        r_ self.get_largest(root.right)

    ___ get_smallest(self, root
        """
        possible dp
        :param root: TreeNode
        :return: integer
        """
        __ not root.left:
            r_ root.val
        r_ self.get_smallest(root.left)



