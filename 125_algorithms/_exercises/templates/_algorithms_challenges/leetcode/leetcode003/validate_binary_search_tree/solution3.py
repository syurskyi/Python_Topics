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
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    ___ isValidBST(self, root
        self.prev = None
        r_ self.is_valid_bst_aux(root)

    ___ is_valid_bst_aux(self, root
        __ root is None:
            r_ True
        ____
            __ not self.is_valid_bst_aux(root.left
                r_ False
            __ self.prev is not None:
                __ self.prev.val >= root.val:
                    r_ False
            self.prev = root
            __ not self.is_valid_bst_aux(root.right
                r_ False
            r_ True
