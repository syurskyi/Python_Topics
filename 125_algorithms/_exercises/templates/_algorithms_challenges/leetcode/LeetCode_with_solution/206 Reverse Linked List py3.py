#!/usr/bin/python3
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you
implement both?
"""


# Definition for singly-linked list.
c_ ListNode:
    ___ - , x):
        val = x
        next = N..


c_ Solution:
    ___ reverseList(self, head: ListNode) -> ListNode:
        prev = N..
        cur = head
        w.... cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        r.. prev

    ___ reverseList_complex(self, head: ListNode) -> ListNode:
        __ n.. head:
            r.. N..

        prev = head
        cur = head.next
        head.next = N..
        w.... prev a.. cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        r.. prev
