"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution:
    ___ buildTree  inorder, postorder):
        """
        Recursive algorithm. Pre-order, in-order, post-order traversal relationship

        in-order:   [left_subtree, root,          right_subtree]
        post-order: [left_subtree, right_subtree, root]

        :param inorder: a list of integers
        :param postorder: a list of integers
        :return: TreeNode root
        """
        __ n.. inorder:
            r.. N..

        root = TreeNode(postorder[-1])
        root_index = inorder.index(root.val)

        root.left = buildTree(inorder[:root_index], postorder[:root_index])
        root.right = buildTree(inorder[root_index+1:], postorder[root_index:-1])

        r.. root