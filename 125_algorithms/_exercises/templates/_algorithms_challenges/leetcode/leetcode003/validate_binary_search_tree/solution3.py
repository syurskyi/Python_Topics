"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
key.
The right subtree of a node contains only nodes with keys greater than the
node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    # @param root, a tree node
    # @return a boolean
    ___ isValidBST  root):
        prev = N..
        r.. is_valid_bst_aux(root)

    ___ is_valid_bst_aux  root):
        __ root __ N..
            r.. T..
        ____:
            __ n.. is_valid_bst_aux(root.left):
                r.. F..
            __ prev __ n.. N..
                __ prev.val >= root.val:
                    r.. F..
            prev = root
            __ n.. is_valid_bst_aux(root.right):
                r.. F..
            r.. T..
