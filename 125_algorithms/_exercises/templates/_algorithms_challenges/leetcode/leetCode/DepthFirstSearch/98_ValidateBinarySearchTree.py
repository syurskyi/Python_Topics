#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ isValidBST  root
        """
        :type root: TreeNode
        :rtype: bool
        """
        # When do inorder traversal, the val growth bigger.
        node_stack   # list
        max_val = "init"
        _____ root or node_stack:
            __ n.. root:
                __ n.. node_stack:
                    r_ True
                node = node_stack.pop()
                __ max_val __ "init" or node.val > max_val:
                    max_val = node.val
                ____
                    r_ False
                root = node.right
            ____
                node_stack.a.. root)
                root = root.left
        r_ True

"""
[]
[1]
[1,null,2,3]
[10,5,15,null,null,6,20]
"""
