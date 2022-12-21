#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ binaryTreePaths  root
        __ n.. root:
            r_ []
        node_stack = [[root, str(root.val)]]
        path_str   # list
        _____ node_stack:
            node, path = node_stack.pop()
            __ node.left:
                new_path = path + "->" + str(node.left.val)
                node_stack.append([node.left, new_path])
            __ node.right:
                new_path = path + "->" + str(node.right.val)
                node_stack.append([node.right, new_path])
            __ n.. node.left a.. n.. node.right:
                path_str.append(path)
        r_ path_str

"""
[]
[1]
[1,2,3,4,null,null,null,5]
"""
