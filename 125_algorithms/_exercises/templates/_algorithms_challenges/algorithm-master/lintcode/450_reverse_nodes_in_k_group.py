"""
Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @param: k: An integer
    @return: a ListNode
    """
    ___ reverseKGroup(self, head, k
        __ not head:
            r_

        dummy = ListNode(0)
        dummy.next = head

        head = dummy
        w___ head:
            head = self.reverse_next_kth(head, k)

        r_ dummy.next

    ___ find_kth(self, head, k
        for i in range(k
            __ not head:
                r_
            head = head.next
        r_ head

    ___ reverse(self, head
        pre = nxt = None
        w___ head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        r_ pre

    ___ reverse_next_kth(self, head, k
        nk = self.find_kth(head, k)
        __ not nk:
            r_
        nk_nxt = nk.next
        n1_pre = head
        n1 = head.next

        nk.next = None

        self.reverse(n1)
        n1_pre.next = nk
        n1.next = nk_nxt
        r_ n1
