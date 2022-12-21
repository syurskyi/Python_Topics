#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ zigzagLevelOrder  root
        __ n.. root:
            r_ []

        left2right = 1
        # 1. scan the level from left to right. -1 reverse.
        ans, stack, temp   # list, [root], []
        _____ stack:
            temp = [node.val ___ node __ stack]
            stack = [child ___ node __ stack
                     ___ child __ (node.left, node.right) __ child]

            ans += [temp[::left2right]]         # Pythonic way
            left2right *= -1

        r_ ans

"""
[]
[1]
[1,2,3]
[0,1,2,3,4,5,6,null,null,7,null,8,9,null,10]
"""
