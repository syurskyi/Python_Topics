"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


c_ Solution:
    """
    @param: head: a ListNode
    @param: k: An integer
    @return: a ListNode
    """
    ___ reverseKGroup  head, k):
        __ n.. head:
            r..

        dummy = ListNode(0)
        dummy.next = head

        head = dummy
        w.... head:
            head = reverse_next_kth(head, k)

        r.. dummy.next

    ___ find_kth  head, k):
        ___ i __ r..(k):
            __ n.. head:
                r..
            head = head.next
        r.. head

    ___ reverse  head):
        pre = nxt = N..
        w.... head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        r.. pre

    ___ reverse_next_kth  head, k):
        nk = find_kth(head, k)
        __ n.. nk:
            r..
        nk_nxt = nk.next
        n1_pre = head
        n1 = head.next

        nk.next = N..

        reverse(n1)
        n1_pre.next = nk
        n1.next = nk_nxt
        r.. n1
