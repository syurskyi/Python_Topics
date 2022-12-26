#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ isSameTree  p, q
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        __ n.. p a.. n.. q:
            r_ True
        __ (n.. p a.. q) or (p a.. n.. q
            r_ F..

        __ p.val != q.val:
            r_ F..
        __ n.. self.isSameTree(p.left, q.left
            r_ F..
        __ n.. self.isSameTree(p.right, q.right
            r_ F..

        r_ True

"""
[]
[1]
[1,2,3]
[1,2,3]
[2,null,3,4,5]
[2,null,3,5,4]
"""
