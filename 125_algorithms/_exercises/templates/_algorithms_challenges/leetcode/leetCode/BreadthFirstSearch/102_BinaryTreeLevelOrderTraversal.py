#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ levelOrder  root
        __ n.. root:
            r_ []

        cur_level, ans = [root], []

        # Breadth-first Search, Pythonic way.
        _____ cur_level:
            ans.a.. [node.val ___ node __ cur_level])
            cur_level = [kid ___ n __ cur_level
                         ___ kid __ (n.left, n.right) __ kid]

        r_ ans

"""
[]
[1]
[1,2,3]
[3,9,20,null,null,15,7]
"""
