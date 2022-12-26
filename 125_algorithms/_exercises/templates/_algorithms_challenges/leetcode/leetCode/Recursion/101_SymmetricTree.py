#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ isSymmetric  root
        r_ self.helper(root, root)

    # If two nodes are symmetric
    ___ helper  lNode, rNode
        __ n.. lNode or n.. rNode:
            r_ lNode __ rNode
        __ lNode.val != rNode.val:
            r_ F..
        r_ (self.helper(lNode.left, rNode.right) a..
                self.helper(lNode.right, rNode.left))

"""
[]
[1]
[1,2,3]
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]
"""
