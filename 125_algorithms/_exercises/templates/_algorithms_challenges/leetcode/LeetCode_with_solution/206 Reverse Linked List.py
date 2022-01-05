"""
Reverse a singly linked list.
"""
__author__ = 'Daniel'


c_ ListNode(o..):
    ___ - , x):
        val = x
        next = N..


c_ Solution(o..):
    ___ reverseList  head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head:
            r.. head

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = pre.next
        w.... pre a.. cur:
            pre, cur.next, cur = cur, pre, cur.next
            # incorrect evaluation order
            # pre, cur, cur.next = cur, cur.next, pre

        dummy.next.next = N..  # original head
        r.. pre  # new head
