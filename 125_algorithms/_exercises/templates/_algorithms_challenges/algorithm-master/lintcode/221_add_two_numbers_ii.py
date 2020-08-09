"""
Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None
"""


class Solution:
    ___ addLists2(self, a, b
        """
        :type a: ListNode
        :type b: ListNode
        :rtype: ListNode
        """
        __ not a and not b:
            r_
        __ not a:
            r_ b
        __ not b:
            r_ a

        a = self.rev_list(a)
        b = self.rev_list(b)

        dummy = tail = ListNode(0)
        carry = 0

        w___ a and b:
            carry += a.val + b.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            a = a.next
            b = b.next
            tail = tail.next

        w___ a:
            carry += a.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            a = a.next
            tail = tail.next

        w___ b:
            carry += b.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            b = b.next
            tail = tail.next

        __ carry:
            tail.next = ListNode(carry)

        r_ self.rev_list(dummy.next)

    ___ rev_list(self, head
        pre = nxt = None

        w___ head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt

        r_ pre
