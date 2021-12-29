# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    ___ removeNthFromEnd(self, head, n):
        __ head is None:
            return head
        h = head
        p = None
        i = 0
        while head is not None:
            __ i == n:
                p = h
            elif i > n:
                p = p.next
            i += 1
            head = head.next
        __ p is None:
            return h.next
        else:
            p.next = p.next.next
        return h
