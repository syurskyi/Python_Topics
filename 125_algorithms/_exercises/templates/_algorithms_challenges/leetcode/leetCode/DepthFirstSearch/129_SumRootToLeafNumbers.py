#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    """
    Depth First Search
    """
    ___ sumNumbers  root
        node_stack   # list
        path_sum = 0
        # Keep the path number from root to the current node.
        cur_node_num = 0

        _____ root or node_stack:
            __ root:
                cur_node_num = cur_node_num * 10 + root.val
                node_stack.a.. [root, cur_node_num])
                root = root.left

            ____
                __ node_stack:
                    pop_record = node_stack.pop()
                    root = pop_record[0].right
                    cur_node_num = pop_record[1]
                    # Meet a leaf node
                    __ n.. pop_record[0].left a.. n.. root:
                        path_sum += cur_node_num

                ____
                    ______
        r_ path_sum

"""
[]
[1,2,3]
[1,null,2,3,null,null,4,5,6]
"""
