"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
__author__ = 'Danyang'


class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ buildTree_MLE(self, preorder, inorder
        """
        Recursive algorithm. Pre-order, in-order, post-order traversal relationship

        pre-order:  [root,         left_subtree,  right_subtree]
        in-order:   [left_subtree, root,          right_subtree]


        recursive algorithm
        :param preorder: a list of integers
        :param inorder: a list of integers
        :return: TreeNode, root
        """
        __ not preorder:
            r_ None

        root = TreeNode(preorder[0])
        root_index = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:root_index+1], inorder[0:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])

        r_ root
        
    ___ buildTree(self, preorder, inorder
        """
        Same idea as the last one, just use integer instead of list
        
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        r_ self._buildTree(0, le.(preorder), 0, le.(inorder))

    ___ _buildTree(self, pre_start, pre_end, in_start, in_end
        __ pre_start >= pre_end:
            r_ None
        root = TreeNode(self.preorder[pre_start])
        offset = self.inorder[in_start:in_end + 1].index(root.val)
        root.left = self._buildTree(pre_start + 1, pre_start + offset + 1, in_start, in_start + offset)
        root.right = self._buildTree(pre_start + offset + 1, pre_end, in_start + offset + 1, in_end)
        r_ root
