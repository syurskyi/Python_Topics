#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    # Breadth First Search
    ___ rightSideView  root
        __ n.. root:
            r_ []
        cur_level = [root]
        next_level   # list
        result   # list
        _____ cur_level:
            ___ node __ cur_level:
                __ node.left:
                    next_level.a.. node.left)
                __ node.right:
                    next_level.a.. node.right)
            result.a.. cur_level[-1].val)
            cur_level = next_level
            next_level   # list
        r_ result

"""
[]
[1,2,3]
[1,2,3,null,4,null,5]
"""
