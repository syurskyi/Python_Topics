#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-09-06 20:03:53


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Merge Sort
c.. Solution o..
    ___ sortList  head
        __ n.. head or n.. head.next:
            r_ head
        # Get the two half parts.
        pre_slow = None
        slow = fast = head
        _____ fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        pre_slow.next = None        # Cut the linked list to two parts.
        left_list = self.sortList(head)
        right_list = self.sortList(slow)
        r_ self.merge(left_list, right_list)

    # Operator merge.
    ___ merge  left_list, right_list
        pre_head = dummy = ListNode(None)
        _____ left_list and right_list:
            __ left_list.val < right_list.val:
                dummy.next = left_list
                left_list = left_list.next
            ____
                dummy.next = right_list
                right_list = right_list.next
            dummy = dummy.next

        dummy.next = left_list or right_list

        r_ pre_head.next


# Quick sort:  Time Limit Exceeded
c.. Solution_2 o..
    ___ partition  begin, end
        __ n.. begin or begin.next __ end:
            r_ begin
        pivot = begin.val
        keep, pos = begin, begin
        scan = begin.next
        _____ scan != end:
            __ scan.val <= pivot:
                pos = pos.next
                __ scan != pos:
                    scan.val, pos.val = pos.val, scan.val
            scan = scan.next

        pos.val, keep.val = keep.val, pos.val
        r_ pos

    ___ quick_sort  begin, end
        __ begin __ end or begin.next __ end:
            r_ begin

        pos = self.partition(begin, end)
        head = self.quick_sort(begin, pos)
        self.quick_sort(pos.next, end)
        r_ head

    ___ sortList  head
        r_ self.quick_sort(head, None)

"""
[]
[1]
[1,2]
[5,1,2]
[5,1,2,3]
[5,1,2,3,6,7,8,9,12,2]
"""
