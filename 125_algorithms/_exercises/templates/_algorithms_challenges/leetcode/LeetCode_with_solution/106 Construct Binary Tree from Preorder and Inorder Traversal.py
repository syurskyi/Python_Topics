"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
__author__ 'Danyang'


c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..


c_ Solution:
    ___ buildTree_MLE  preorder, inorder
        """
        Recursive algorithm. Pre-order, in-order, post-order traversal relationship

        pre-order:  [root,         left_subtree,  right_subtree]
        in-order:   [left_subtree, root,          right_subtree]


        recursive algorithm
        :param preorder: a list of integers
        :param inorder: a list of integers
        :return: TreeNode, root
        """
        __ n.. preorder:
            r.. N..

        root TreeNode(preorder 0
        root_index inorder.i.. root.val)

        root.left buildTree(preorder[1:root_index+1], inorder[0:root_index])
        root.right buildTree(preorder[root_index+1:], inorder[root_index+1:])

        r.. root
        
    ___ buildTree  preorder, inorder
        """
        Same idea as the last one, just use integer instead of list
        
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder preorder
        inorder inorder
        r.. _buildTree(0, l..(preorder), 0, l..(inorder

    ___ _buildTree  pre_start, pre_end, in_start, in_end
        __ pre_start >_ pre_end:
            r.. N..
        root TreeNode(preorder[pre_start])
        offset inorder[in_start:in_end + 1].i.. root.val)
        root.left _buildTree(pre_start + 1, pre_start + offset + 1, in_start, in_start + offset)
        root.right _buildTree(pre_start + offset + 1, pre_end, in_start + offset + 1, in_end)
        r.. root
