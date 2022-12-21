#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c.. Solution o..
    ___ swapPairs  head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = before_node = ListNode(0)
        before_node.next = head

        """
        Given a situation    : ... -> B -> | C -> D | -> E -> ...
        Node before C is swaped, and then we should swap C and D,
        so the result is     : ... -> B -> | D -> C | -> E -> ...
        Assume B is before_node, C is head, then we need to:
            1. B.next = D     ( B -> D, C -> D, D -> E)
            2. D.next = C     ( B -> D, D -> C,   -> E)
            3. C.next = E     ( B -> D, D -> C, C -> E)

        """
        _____ head:
            __ head.next:
                next_node = head.next.next       # Keep E
                before_node.next = head.next     # Step 1
                head.next.next = head            # Step 2
                head.next = next_node            # Step 3

                # Scan next two node
                before_node = head
                head = head.next
            ____
                break
        r_ result.next

"""
[]
[1]
[1,2,3]
[1,2,3,4,5,6]
"""
