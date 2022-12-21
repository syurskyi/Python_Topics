#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    # Easy to understand
    ___ lowestCommonAncestor  root, p, q
        min_val = min(p.val, q.val)
        max_val = m..(p.val, q.val)
        _____ root:
            value = root.val
            __ min_val <= value <= max_val:
                r_ root
            ____ max_val < value:
                root = root.left
            ____
                root = root.right
        r_ None


c.. Solution_2 o..
    """
    One elegant code, some puzzling but short code. according to:
    https://leetcode.com/discuss/44959/3-lines-with-o-1-space-1-liners-alternatives
    Just walk down from the whole tree's root as long as
    both p and q are in the same subtree
    """
    ___ lowestCommonAncestor  root, p, q
        _____ (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        r_ root
