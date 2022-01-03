"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


c_ Solution:
    ___ addLists2(self, a, b):
        """
        :type a: ListNode
        :type b: ListNode
        :rtype: ListNode
        """
        __ n.. a a.. n.. b:
            r..
        __ n.. a:
            r.. b
        __ n.. b:
            r.. a

        a = rev_list(a)
        b = rev_list(b)

        dummy = tail = ListNode(0)
        carry = 0

        w.... a a.. b:
            carry += a.val + b.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            a = a.next
            b = b.next
            tail = tail.next

        w.... a:
            carry += a.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            a = a.next
            tail = tail.next

        w.... b:
            carry += b.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            b = b.next
            tail = tail.next

        __ carry:
            tail.next = ListNode(carry)

        r.. rev_list(dummy.next)

    ___ rev_list(self, head):
        pre = nxt = N..

        w.... head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt

        r.. pre
