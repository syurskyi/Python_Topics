"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @param: k: An integer
    @return: a ListNode
    """
    ___ reverseKGroup(self, head, k):
        __ n.. head:
            r..

        dummy = ListNode(0)
        dummy.next = head

        head = dummy
        while head:
            head = self.reverse_next_kth(head, k)

        r.. dummy.next

    ___ find_kth(self, head, k):
        ___ i __ r..(k):
            __ n.. head:
                r..
            head = head.next
        r.. head

    ___ reverse(self, head):
        pre = nxt = N..
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        r.. pre

    ___ reverse_next_kth(self, head, k):
        nk = self.find_kth(head, k)
        __ n.. nk:
            r..
        nk_nxt = nk.next
        n1_pre = head
        n1 = head.next

        nk.next = N..

        self.reverse(n1)
        n1_pre.next = nk
        n1.next = nk_nxt
        r.. n1
