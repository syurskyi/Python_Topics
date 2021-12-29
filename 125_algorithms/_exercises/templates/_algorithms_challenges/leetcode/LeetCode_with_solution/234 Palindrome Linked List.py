"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""
__author__ = 'Daniel'


class ListNode:
    ___ __init__(self, x):
        self.val = x
        self.next = N..


class Solution:
    ___ isPalindrome(self, head):
        """
        Algorithms:
        1. put into array O(N)
        2. midpoint, reverse the other - O(n) time and O(1) space

        :type head: ListNode
        :rtype: bool
        """
        n = self.l..(head)
        m = n/2
        mid = self.get(head, m)
        __ n%2 != 0:
            mid = mid.next

        mid = self.reverse(mid)
        while head and mid:
            __ head.val != mid.val:
                r.. False
            head = head.next
            mid = mid.next

        r.. True

    ___ l..(self, head):
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next

        r.. cnt

    ___ get(self, head, n):
        cnt = 0
        cur = head
        while cnt < n:
            cnt += 1
            cur = cur.next

        r.. cur

    ___ reverse(self, head):
        __ n.. head:
            r.. head

        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, dummy.next
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        __ head: head.next = N..
        r.. pre
