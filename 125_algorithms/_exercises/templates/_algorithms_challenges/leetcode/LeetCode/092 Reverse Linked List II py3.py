#!/usr/bin/python3
"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None


class Solution:
    ___ reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = None
        cur = head

        l = 1
        w___ l < m:
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

        w___ l <= n:  # notice is it <=
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
        r_ head
