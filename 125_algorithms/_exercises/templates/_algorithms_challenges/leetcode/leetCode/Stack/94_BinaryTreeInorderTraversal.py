#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c.. Solution o..
    ___ inorderTraversal  root
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        __ n.. root:
            r_ []

        tree_stack   # list
        inorder_tra   # list
        _____ root or tree_stack:
            # Go along the left child
            __ root:
                tree_stack.a.. root)
                root = root.left
            # Meet a left, go back to the parent node
            ____
                __ n.. tree_stack:
                    root = None
                    c_
                node = tree_stack.pop()
                inorder_tra.a.. node.val)
                root = node.right

        r_ inorder_tra

"""
[]
[1]
[1,2,3,null,null,4,null,null,5]
"""
