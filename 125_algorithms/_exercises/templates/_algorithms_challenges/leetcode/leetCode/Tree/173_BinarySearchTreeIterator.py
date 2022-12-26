#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c.. BSTIterator o..
    ___ __init__  root
        self.root = root
        self.node_stack   # list
        self.cur_node = root

    ___ hasNext(self
        __ self.cur_node or self.node_stack:
            r_ True
        ____
            r_ F..

    ___ next(self
        # inorder traversal
        _____ self.cur_node:
            self.node_stack.a.. self.cur_node)
            self.cur_node = self.cur_node.left

        top = self.node_stack.pop()
        self.cur_node = top.right
        r_ top.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

"""
[]
[1]
[10,8,16,2,9,15,17]
"""
