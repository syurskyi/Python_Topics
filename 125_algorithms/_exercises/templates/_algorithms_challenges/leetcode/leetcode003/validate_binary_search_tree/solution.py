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
    ___ isValidBST(self, root):
        __ root __ N..
            r.. T..
        ____:
            left = T..
            right = T..
            __ root.left __ n.. N..
                left = (max_node(root.left).val < root.val
                        a.. isValidBST(root.left))
            __ root.right __ n.. N..
                right = (min_node(root.right).val > root.val
                         a.. isValidBST(root.right))
            __ left a.. right:
                r.. T..
            r.. F..

    ___ min_node(self, root):
        w.... root.left __ n.. N..
            root = root.left
        r.. root

    ___ max_node(self, root):
        w.... root.right __ n.. N..
            root = root.right
        r.. root
