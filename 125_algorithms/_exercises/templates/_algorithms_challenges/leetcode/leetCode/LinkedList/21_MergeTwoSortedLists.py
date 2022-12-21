#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Recursive way.
c.. Solution o..
    ___ mergeTwoLists  l1, l2
        __ n.. l1:
            r_ l2
        __ n.. l2:
            r_ l1
        merged_head = None
        __(l1.val <= l2.val
            merged_head = l1
            merged_head.next = self.mergeTwoLists(l1.next, l2)
        ____
            merged_head = l2
            merged_head.next = self.mergeTwoLists(l1, l2.next)
        r_ merged_head


# Iteratively
c.. Solution_2 o..
    ___ mergeTwoLists  l1, l2
        merged_list = ListNode(0)
        merged_head = merged_list

        # Scan through l1 and l2, get the smaller one to merged list
        _____ l1 a.. l2:
            __ l1.val <= l2.val:
                merged_list.next = l1
                l1 = l1.next

            ____
                merged_list.next = l2
                l2 = l2.next
            merged_list = merged_list.next

        # l2 has gone to the tail already and only need to scan l1
        _____ l1:
            merged_list.next = l1
            l1 = l1.next
            merged_list = merged_list.next

        # l1 has gone to the tail already and only need to scan l2
        _____ l2:
            merged_list.next = l2
            l2 = l2.next
            merged_list = merged_list.next

        r_ merged_head.next

"""
[]
[]
[1,4,8,12]
[2,3]
[1,3,5,7,9]
[2,4,6,8,10]
"""
