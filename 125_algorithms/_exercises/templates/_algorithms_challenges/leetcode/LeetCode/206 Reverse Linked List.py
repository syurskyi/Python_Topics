"""
Reverse a singly linked list.
"""
__author__ = 'Daniel'


class ListNode(object
    ___ __init__(self, x
        self.val = x
        self.next = None


class Solution(object
    ___ reverseList(self, head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ not head:
            r_ head

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = pre.next
        w___ pre and cur:
            pre, cur.next, cur = cur, pre, cur.next
            # incorrect evaluation order
            # pre, cur, cur.next = cur, cur.next, pre

        dummy.next.next = None  # original head
        r_ pre  # new head
