#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c.. Solution o..
    ___ flatten  root
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        __ n.. root:
            r_ None

        self.get_list(root)

    # Flatten the tree to a linked list in-place, and return it's tail.
    ___ get_list  root
        left_child = root.left
        right_child = root.right

        # Leaf node: do nothing, and the linked list has just one node.
        __ n.. left_child a.. n.. right_child:
            r_ root

        # Have left child node, move it to the next node in the linked list.
        # Flatten the left subtree and then get the tail
        # of the flattened subtree's linked list. Make the right child go after
        # the tail, and flatten the right subtree at last.
        __ left_child:
            root.left = None
            root.right = left_child
            left_tail_node = self.get_list(left_child)

            __ right_child:
                left_tail_node.right = right_child
                r_ self.get_list(right_child)
            ____
                r_ left_tail_node
        # No left child node, just flatten the right node.
        ____
            r_ self.get_list(right_child)

"""
[]
[1,2,3,null,null,4,5]
[1,2,5,3,4,null,6]
"""
