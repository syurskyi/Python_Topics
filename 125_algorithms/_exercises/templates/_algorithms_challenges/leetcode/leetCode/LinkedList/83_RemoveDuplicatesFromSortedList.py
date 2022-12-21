#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-04-29 16:18:37


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Recursively
c.. Solution_2 o..
    ___ deleteDuplicates  head
        __ n.. head or n.. head.next:
            r_ head
        head.next = self.deleteDuplicates(head.next)
        r_ head.next __ head.val __ head.next.val else head


# Iteratively
c.. Solution o..
    ___ deleteDuplicates  head
        cur = head
        _____ cur:
            # Skip all the duplicated nodes of cur.
            _____ cur.next a.. cur.val __ cur.next.val:
                cur.next = cur.next.next
            # No duplicated nodes, move cur to next node
            cur = cur.next

        r_ head

"""
[]
[1]
[3,3,3,3,3]
[1,1,1,2,3,4,4,4,4,5]
"""
