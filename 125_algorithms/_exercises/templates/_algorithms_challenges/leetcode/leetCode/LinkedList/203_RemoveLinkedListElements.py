#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c.. Solution o..
    ___ removeElements  head, val
        pre_node = dummy = ListNode(0)
        _____ head:
            __ head.val __ val:
                pre_node.next = None
            ____
                pre_node.next = head
                pre_node = head
            head = head.next
        r_ dummy.next

"""
[]
1
[1,1,1]
1
[1,2,3]
2
[1,2]
2
"""
