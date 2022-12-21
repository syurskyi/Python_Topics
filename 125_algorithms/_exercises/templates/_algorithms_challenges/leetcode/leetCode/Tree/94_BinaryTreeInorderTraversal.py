#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c.. Solution o..
    # iteratively
    ___ inorderTraversal  root
        tree_stack   # list
        inorder_tra   # list
        _____ root or tree_stack:
            # Go along the left child
            __ root:
                tree_stack.append(root)
                root = root.left
            # Meet a left, go back to the parent node
            ____
                node = tree_stack.pop()
                inorder_tra.append(node.val)
                root = node.right

        r_ inorder_tra


c.. Solution_2 o..
    # recursively
    ___ inorderTraversal  root
        inorder_tra   # list
        self.helper(root, inorder_tra)
        r_ inorder_tra

    ___ helper  root, inorder_tra
        __ root:
            self.helper(root.left, inorder_tra)
            inorder_tra.append(root.val)
            self.helper(root.right, inorder_tra)

"""
[]
[1]
[1,2,3,null,null,4,null,null,5]
"""
