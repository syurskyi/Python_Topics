# -*- coding: utf-8 -*-
"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
__author__ 'Daniel'


c_ ListNode:
    ___ - , x
        val x
        next N..


c_ Solution:
    ___ getIntersectionNode  headA, headB
        """
        We can do something with the length difference.

        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        l_a _get_len(headA)
        l_b _get_len(headB)
        __ l_a > l_b:
            l_a, l_b l_b, l_a
            headA, headB headB, headA

        cur_a headA
        cur_b headB
        ___ i __ x..(l_b-l_a
            cur_b cur_b.next

        w.... cur_a !_ cur_b:
            cur_a cur_a.next
            cur_b cur_b.next

        r.. cur_a

    ___ _get_len  head
        n 0
        cur head
        w.... cur:
            n += 1
            cur cur.next

        r.. n