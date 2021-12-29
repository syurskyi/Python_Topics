# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    ___ removeNthFromEnd(self, head, n):
        __ head __ N..
            r.. N..
        ____ n __ 0:
            r.. head
        ____:
            q = p = pp = head  # `pp` is the node preceding `p`
            while q __ n.. N..
                __ n <= 0:
                    pp = p
                    p = p.next
                q = q.next
                n -= 1
            # Remove the head node
            __ pp __ p:
                head = pp.next
            ____:
                pp.next = p.next
                # Free p
            r.. head
