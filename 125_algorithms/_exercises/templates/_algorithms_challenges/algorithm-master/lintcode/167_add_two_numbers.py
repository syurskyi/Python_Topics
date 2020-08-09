"""
Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None
"""


class Solution:
    ___ addLists(self, A, B
        """
        :type A: ListNode
        :type B: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(-1)
        carry = 0

        w___ A and B:
            carry += A.val + B.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            A = A.next
            B = B.next

        w___ A:
            carry += A.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            A = A.next

        w___ B:
            carry += B.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            B = B.next

        __ carry:
            tail.next = ListNode(carry)

        r_ dummy.next
