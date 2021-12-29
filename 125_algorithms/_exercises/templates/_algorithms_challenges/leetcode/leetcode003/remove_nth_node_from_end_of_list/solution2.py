# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    ___ removeNthFromEnd(self, head, n):
        __ head __ N..
            r.. head
        h = head
        p = N..
        i = 0
        while head __ n.. N..
            __ i __ n:
                p = h
            ____ i > n:
                p = p.next
            i += 1
            head = head.next
        __ p __ N..
            r.. h.next
        ____:
            p.next = p.next.next
        r.. h
