# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    ___ swapPairs(self, head):
        __ head __ None or head.next __ None:
            return head
        else:
            t = head.next
            head.next = self.swapPairs(t.next)
            t.next = head
            return t
