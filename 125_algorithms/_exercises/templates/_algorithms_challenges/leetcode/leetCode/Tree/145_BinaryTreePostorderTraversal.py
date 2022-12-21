#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    # Postorder Traversal
    ___ postorderTraversal  root
        __ n.. root:
            r_ []
        result   # list
        node_stack   # list
        _____ root or node_stack:
            __ root:
                node_stack.append(root)
                result.append(root.val)
                root = root.right
            ____
                node = node_stack.pop()
                root = node.left
        r_ result[::-1]

"""
[]
[1, null, 2, 3]
[1, null, 2, 3, null, 4, 5]
"""
