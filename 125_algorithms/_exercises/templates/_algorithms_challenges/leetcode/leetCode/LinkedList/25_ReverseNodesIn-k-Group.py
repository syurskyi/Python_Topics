#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


c.. Solution o..
    ___ reverseKGroup  head, k
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        __ n.. head or k <= 1:
            r_ head

        solution = ListNode(0)
        solution.next = head
        before_node = solution
        count = 0

        # Get each k nodes and reverse all of them
        _____ head:
            count += 1
            __ count % k __ 0:
                after_node = head.next
                before_node = self.reverse_k_nodes(before_node, after_node)
                head = after_node
            ____
                head = head.next

        r_ solution.next

    ___ reverse_k_nodes  before_node, after_node
        """
        Given a situation    : ... -> B -> | C -> ... -> X | -> Y -> ...
        Nodes before C is swaped, and then we should swap node between C and X,
        so the result is     : ... -> B -> | X -> ... -> C | -> Y -> ...
        Then what we need to is:
            1. Get node C and make it as tail in k-reversed-list:  C
            2. Get all the other nodes and put each before the
               head of current k-reversed-list:  X -> ... ->C
            3. Make B.next = X and C.next = Y:
                -> B -> | X -> ... -> C  | -> Y
        """
        __ before_node.next __ after_node:
            pass

        # Step 2
        head = before_node.next
        reversed_list_head = reversed_list_tail = head
        cur_node = head.next
        _____ cur_node != after_node:
            keep_node = cur_node.next
            cur_node.next = reversed_list_head
            reversed_list_head = cur_node
            cur_node = keep_node

        # Step 3
        before_node.next = reversed_list_head
        reversed_list_tail.next = after_node
        r_ reversed_list_tail

"""
[]
1
[1]
1
[1,2,3,4,5,6,7,8,9]
4
"""
