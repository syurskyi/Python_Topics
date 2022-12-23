#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    # Preorder Traversal
    ___ preorderTraversal  root
        __ n.. root:
            r_ []
        result   # list
        node_stack   # list
        _____ root or node_stack:
            __ root:
                node_stack.a.. root)
                result.a.. root.val)
                root = root.left
            ____
                node = node_stack.pop()
                root = node.right
        r_ result

"""
[]
[1, null, 2, 3]
[1, null, 2, 3, null, 4, 5]
"""
