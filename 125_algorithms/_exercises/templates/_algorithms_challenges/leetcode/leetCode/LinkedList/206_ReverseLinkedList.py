#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c.. Solution o..
    # recursively reverse
    ___ reverseList  head
        __ n.. head or n.. head.next:
            r_ head
        reverse_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        r_ reverse_head

    # iteratively reverse
    ___ reverseList_2  head
        reverse_head = None
        _____ head:
            next_node = head.next
            head.next = reverse_head
            reverse_head = head
            head = next_node
        r_ reverse_head

"""
[]
[1]
[1,2]
[1,2,3,4,5]
"""
