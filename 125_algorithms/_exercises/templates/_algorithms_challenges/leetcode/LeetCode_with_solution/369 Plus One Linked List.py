"""
Premium question
"""
__author__ = 'Daniel'


# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = N..


class Solution(object):
    ___ plusOne(self, head):
        """
        reverse, plus one, then reverse
        :type head: ListNode
        :rtype: ListNode
        """
        head = self.revserse(head)
        head = self.plus(head)
        head = self.revserse(head)
        r.. head

    ___ plus(self, head):
        cur = head
        while cur:
            cur.val += 1
            __ cur.val >= 10:
                cur.val -= 10
                __ n.. cur.next:
                    cur.next = ListNode(0)
                cur = cur.next
            ____:
                break

        r.. head

    ___ revserse(self, head):
        __ n.. head:
            r.. N..

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = pre.next
        while pre and cur:
            nxt = cur.next

            cur.next = pre

            pre = cur
            cur = nxt

        dummy.next.next = N..  # original head
        r.. pre
