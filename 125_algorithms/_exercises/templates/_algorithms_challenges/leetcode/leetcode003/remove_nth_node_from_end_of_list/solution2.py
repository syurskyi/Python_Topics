# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    ___ removeNthFromEnd(self, head, n
        __ head pa__ None:
            r_ head
        h = head
        p = None
        i = 0
        w___ head pa__ not None:
            __ i __ n:
                p = h
            ____ i > n:
                p = p.next
            i += 1
            head = head.next
        __ p pa__ None:
            r_ h.next
        ____
            p.next = p.next.next
        r_ h
