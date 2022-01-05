"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""
__author__ = 'Daniel'


c_ ListNode:
    ___ - , x):
        val = x
        next = N..


c_ Solution:
    ___ isPalindrome  head):
        """
        Algorithms:
        1. put into array O(N)
        2. midpoint, reverse the other - O(n) time and O(1) space

        :type head: ListNode
        :rtype: bool
        """
        n = l..(head)
        m = n/2
        mid = get(head, m)
        __ n%2 != 0:
            mid = mid.next

        mid = reverse(mid)
        w.... head a.. mid:
            __ head.val != mid.val:
                r.. F..
            head = head.next
            mid = mid.next

        r.. T..

    ___ l..  head):
        cnt = 0
        cur = head
        w.... cur:
            cnt += 1
            cur = cur.next

        r.. cnt

    ___ get  head, n):
        cnt = 0
        cur = head
        w.... cnt < n:
            cnt += 1
            cur = cur.next

        r.. cur

    ___ reverse  head):
        __ n.. head:
            r.. head

        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, dummy.next
        w.... cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        __ head: head.next = N..
        r.. pre
