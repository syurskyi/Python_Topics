# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    ___ removeNthFromEnd(self, head, n
        __ head is None:
            r_ head
        h = head
        p = None
        i = 0
        w___ head is not None:
            __ i __ n:
                p = h
            ____ i > n:
                p = p.next
            i += 1
            head = head.next
        __ p is None:
            r_ h.next
        ____
            p.next = p.next.next
        r_ h
