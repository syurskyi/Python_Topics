#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Refer to:
# https://leetcode.com/discuss/38930/concise-java-solutions-o-log-n-2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c.. Solution o..
    ___ countNodes  root
        __ n.. root:
            r_ 0
        node_nums = 0
        tree_height = self.getHeight(root)
        _____ root:
            __ self.getHeight(root.right) __ tree_height - 1:
                # root.left's subtree is a full complete binary tree
                # and it's height is tree_height-1
                node_nums += 1 << tree_height
                root = root.right
            ____
                # root.right's subtree is a full complete binary tree
                # and it's height is tree_height-2
                node_nums += 1 << (tree_height-1)
                root = root.left

            tree_height -= 1

        r_ node_nums

    # Get complete BT's height, assume the root is height 0, increment then.
    ___ getHeight  root
        __ n.. root:
            r_ -1
        height = 0
        _____ root.left:
            root = root.left
            height += 1
        r_ height

"""
[]
[1]
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5]
"""
