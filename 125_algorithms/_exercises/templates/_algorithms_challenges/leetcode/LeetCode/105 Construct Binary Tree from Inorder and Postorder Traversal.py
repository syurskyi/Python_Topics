"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ___ buildTree(self, inorder, postorder
        """
        Recursive algorithm. Pre-order, in-order, post-order traversal relationship

        in-order:   [left_subtree, root,          right_subtree]
        post-order: [left_subtree, right_subtree, root]

        :param inorder: a list of integers
        :param postorder: a list of integers
        :return: TreeNode root
        """
        __ not inorder:
            r_ None

        root = TreeNode(postorder[-1])
        root_index = inorder.index(root.val)

        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])

        r_ root