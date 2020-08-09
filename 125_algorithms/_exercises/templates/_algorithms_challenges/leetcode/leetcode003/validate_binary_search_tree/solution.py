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
        __ root is None:
            r_ True
        ____
            left = True
            right = True
            __ root.left is not None:
                left = (self.max_node(root.left).val < root.val
                        and self.isValidBST(root.left))
            __ root.right is not None:
                right = (self.min_node(root.right).val > root.val
                         and self.isValidBST(root.right))
            __ left and right:
                r_ True
            r_ False

    ___ min_node(self, root
        w___ root.left is not None:
            root = root.left
        r_ root

    ___ max_node(self, root
        w___ root.right is not None:
            root = root.right
        r_ root
