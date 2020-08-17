# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    ___ swapPairs(self, head
        __ head pa__ None or head.next pa__ None:
            r_ head
        ____
            t = head.next
            head.next = self.swapPairs(t.next)
            t.next = head
            r_ t
