#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
c.. ListNode o..
    ___ __init__  x
        self.val = x
        self.next = None


c.. Solution o..
    ___ addTwoNumbers  l1, l2
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_in = 0
        head = ListNode(0)
        l_sum = head

        _____ l1 and l2:
            l_sum.next = ListNode((l1.val + l2.val + carry_in) % 10)
            carry_in = (l1.val + l2.val + carry_in) / 10
            l1 = l1.next
            l2 = l2.next
            l_sum = l_sum.next

        __ l1:
            _____ l1:
                l_sum.next = ListNode((l1.val + carry_in) % 10)
                carry_in = (l1.val + carry_in) / 10
                l1 = l1.next
                l_sum = l_sum.next

        __ l2:
            _____ l2:
                l_sum.next = ListNode((l2.val + carry_in) % 10)
                carry_in = (l2.val + carry_in) / 10
                l2 = l2.next
                l_sum = l_sum.next

        __ carry_in != 0:
            l_sum.next = ListNode(carry_in)

        r_ head.next
