#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ hasPathSum  root, s..
        __ n.. root:
            r_ False

        root_val = root.val
        __ root.left and self.hasPathSum(root.left, s..-root_val
            r_ True
        __ root.right and self.hasPathSum(root.right, s..-root_val
            r_ True
        __ n.. root.left and n.. root.right and s.. __ root.val:
            r_ True
        r_ False

"""
[]
0
[1,2,3,4,null,6,7,5,8]
15
[1,2,2,3,null,null,3,4,null,null,4]
9
"""
