#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ minDepth  root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r_ 0

        __ root.left a.. root.right:
            r_ 1 + m.. self.minDepth(root.left), self.minDepth(root.right))
        __ n.. root.left:
            r_ 1 + self.minDepth(root.right)
        __ n.. root.right:
            r_ 1 + self.minDepth(root.left)
        ____
            r_ 1

"""
[]
[1]
[1,2,null,3]
[1,2,3,4,null,6,7,5,8]
[1,2,2,3,null,null,3,4,null,null,4]
"""
