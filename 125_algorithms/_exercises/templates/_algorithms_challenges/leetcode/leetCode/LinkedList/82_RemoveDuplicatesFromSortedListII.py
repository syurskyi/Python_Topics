#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-04-29 17:15:38


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Recursively
c.. Solution o..
    ___ deleteDuplicates  head
        __ n.. head or n.. head.next:
            r_ head
        __ head.val __ head.next.val:
            _____ head.next and head.val __ head.next.val:
                head = head.next
            r_ self.deleteDuplicates(head.next)
        ____
            head.next = self.deleteDuplicates(head.next)
            r_ head


# Iteraively
c.. Solution_2 o..
    ___ deleteDuplicates  head
        cur = pre_head = ListNode(0)
        _____ head:
            __ head.next and head.val __ head.next.val:
                # Skip the duplicated nodes.
                _____ head.next and head.val __ head.next.val:
                    head = head.next
                head = head.next
            # we can make sure head is one single node here.
            ____
                cur.next = head
                cur = cur.next
                head = head.next
        cur.next = None     # Make sure the cur here is the tail: [1,2,2]
        r_ pre_head.next

"""
[]
[1]
[1,2,2]
[3,3,3,3,3]
[1,1,1,2,3,4,4,4,4,5]
"""
