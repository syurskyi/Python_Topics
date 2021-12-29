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

class Solution:
    # @param root, a tree node
    # @return a boolean
    ___ isValidBST(self, root):
        self.prev = N..
        r.. self.is_valid_bst_aux(root)

    ___ is_valid_bst_aux(self, root):
        __ root __ N..
            r.. True
        ____:
            __ n.. self.is_valid_bst_aux(root.left):
                r.. False
            __ self.prev __ n.. N..
                __ self.prev.val >= root.val:
                    r.. False
            self.prev = root
            __ n.. self.is_valid_bst_aux(root.right):
                r.. False
            r.. True
