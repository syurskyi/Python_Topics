#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


c.. Solution o..
    ___ connect  root
        __ n.. root:
            r_ None

        cur_head = root
        next_head = None
        # Breadth-first Scan
        _____ cur_head:
            # Get the next node cur_head's child point to.
            next_node = cur_head.next
            _____ next_node:
                __ next_node.left:
                    next_node = next_node.left
                    break
                __ next_node.right:
                    next_node = next_node.right
                    break
                next_node = next_node.next

            __ cur_head.left:
                __ n.. next_head:
                    next_head = cur_head.left
                __ cur_head.right:
                    cur_head.left.next = cur_head.right
                ____
                    cur_head.left.next = next_node
            __ cur_head.right:
                __ n.. next_head:
                    next_head = cur_head.right
                cur_head.right.next = next_node
            cur_head = cur_head.next

            # Go to next level.
            __ n.. cur_head:
                cur_head = next_head
                next_head = None

""" Readable implementation
class Solution(object):
    def connect(self, root):
        # For all the non-empty nodes:
        #     node.left.next = right(or next_node)
        #     node.right.next = next_node, (or right)
        if not root:
            return None

        next_node = root.next
        while next_node:
            if next_node.left:
                next_node = next_node.left
                break
            if next_node.right:
                next_node = next_node.right
                break
            next_node = next_node.next

        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = next_node

        if root.right:
            root.right.next = next_node

        # Get root.right done firstly because when we compute root.left,
        # we may use the node's next relationship in connect(root.right).
        self.connect(root.right)
        self.connect(root.left)
"""

"""
[0]
[1,2,3,4,5,null,7]
"""
