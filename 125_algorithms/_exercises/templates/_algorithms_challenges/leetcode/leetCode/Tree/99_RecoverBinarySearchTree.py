#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    conflict_first = None
    conflict_second = None
    pre_node = None

    ___ recoverTree  root
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        __ n.. root:
            r_ None

        self.find_conflict(root)

        self.conflict_first.val, self.conflict_second.val = (
            self.conflict_second.val, self.conflict_first.val)

    # Do the inorder traversal and when find a decreasing pair,
    # then we find one (maybe all the two) node which is swapped.
    ___ find_conflict  root
        __ root.left:
            self.find_conflict(root.left)

        __ self.pre_node a.. root.val < self.pre_node.val:
            __ n.. self.conflict_first:
                self.conflict_first = self.pre_node
            self.conflict_second = root

        self.pre_node = root
        __ root.right:
            self.find_conflict(root.right)
"""
[0,1]
[8,9,13,2,6,4,14]
[9,4,13,2,6,8,14]
"""
