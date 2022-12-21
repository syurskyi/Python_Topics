#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c.. Solution o..
    ___ insertionSortList  head
        __ n.. head or n.. head.next:
            r_ head

        dummy = ListNode(0)
        start = dummy
        _____ head:
            cur_node = head
            head = head.next
            # Don't need to scan from head of the sorted list every time.
            __ start.val > cur_node.val:
                start = dummy
            # Find the insert position.
            _____ start.next and start.next.val < cur_node.val:
                start = start.next
            # Insert the current node.
            cur_node.next = start.next
            start.next = cur_node

        r_ dummy.next
"""
[]
[1]
[1,2]
[5,1,2]
[5,1,2,3]
"""
