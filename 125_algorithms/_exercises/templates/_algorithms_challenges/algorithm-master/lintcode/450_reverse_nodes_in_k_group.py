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
        __ not head:
            return

        dummy = ListNode(0)
        dummy.next = head

        head = dummy
        while head:
            head = self.reverse_next_kth(head, k)

        return dummy.next

    ___ find_kth(self, head, k):
        for i in range(k):
            __ not head:
                return
            head = head.next
        return head

    ___ reverse(self, head):
        pre = nxt = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre

    ___ reverse_next_kth(self, head, k):
        nk = self.find_kth(head, k)
        __ not nk:
            return
        nk_nxt = nk.next
        n1_pre = head
        n1 = head.next

        nk.next = None

        self.reverse(n1)
        n1_pre.next = nk
        n1.next = nk_nxt
        return n1
