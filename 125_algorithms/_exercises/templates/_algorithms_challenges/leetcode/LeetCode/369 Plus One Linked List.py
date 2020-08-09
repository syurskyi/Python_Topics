"""
Premium question
"""
__author__ = 'Daniel'


# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x
        self.val = x
        self.next = None


class Solution(object
    ___ plusOne(self, head
        """
        reverse, plus one, then reverse
        :type head: ListNode
        :rtype: ListNode
        """
        head = self.revserse(head)
        head = self.plus(head)
        head = self.revserse(head)
        r_ head

    ___ plus(self, head
        cur = head
        w___ cur:
            cur.val += 1
            __ cur.val >= 10:
                cur.val -= 10
                __ not cur.next:
                    cur.next = ListNode(0)
                cur = cur.next
            ____
                break

        r_ head

    ___ revserse(self, head
        __ not head:
            r_ None

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = pre.next
        w___ pre and cur:
            nxt = cur.next

            cur.next = pre

            pre = cur
            cur = nxt

        dummy.next.next = None  # original head
        r_ pre
