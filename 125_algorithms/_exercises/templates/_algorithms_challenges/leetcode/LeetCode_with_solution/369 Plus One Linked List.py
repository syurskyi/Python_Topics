"""
Premium question
"""
__author__ = 'Daniel'


# Definition for singly-linked list.
c_ ListNode(object):
    ___ - , x):
        val = x
        next = N..


c_ Solution(object):
    ___ plusOne(self, head):
        """
        reverse, plus one, then reverse
        :type head: ListNode
        :rtype: ListNode
        """
        head = revserse(head)
        head = plus(head)
        head = revserse(head)
        r.. head

    ___ plus(self, head):
        cur = head
        w.... cur:
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
        w.... pre a.. cur:
            nxt = cur.next

            cur.next = pre

            pre = cur
            cur = nxt

        dummy.next.next = N..  # original head
        r.. pre
