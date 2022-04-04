#!/usr/bin/python3
"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
c_ ListNode:
    ___ - , x
        val = x
        next = N..


c_ Solution:
    ___ reverseBetween  head: ListNode, m: i.., n: i..) __ ListNode:
        prev = N..
        cur = head

        l = 1
        w.... l < m:
            nxt = cur.next
            prev = cur
            cur = nxt
            l += 1
        #           prev    cur (m)
        # -> ... -> left -> right -> ... -> null
        #                                    (n)
        # -> ... -> left <- right <- ... <- prev <- cur -> ... -> null
        # -> ... -> left -> prev -> ... -> right -> cur -> ... -> null
        leftend = prev
        rightend = cur

        w.... l <= n:  # notice is it <=
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            l += 1

        __ m != 1:  # leftend is None
            leftend.next = prev
        ____
            head = prev

        rightend.next = cur
        r.. head
