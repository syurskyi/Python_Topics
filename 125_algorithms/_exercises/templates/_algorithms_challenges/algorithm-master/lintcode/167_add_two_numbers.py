"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


c_ Solution:
    ___ addLists(self, A, B):
        """
        :type A: ListNode
        :type B: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(-1)
        carry = 0

        w.... A a.. B:
            carry += A.val + B.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            A = A.next
            B = B.next

        w.... A:
            carry += A.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            A = A.next

        w.... B:
            carry += B.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            B = B.next

        __ carry:
            tail.next = ListNode(carry)

        r.. dummy.next
