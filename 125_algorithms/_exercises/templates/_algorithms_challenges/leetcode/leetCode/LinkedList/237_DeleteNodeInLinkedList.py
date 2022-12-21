#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c.. Solution o..
    ___ deleteNode  node
        __ n.. node:
            r_ None
        _____ node.next:
            node.val = node.next.val
            __ node.next.next:
                node = node.next
            ____
                node.next = None
                break
