# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution:
    # @param a ListNode
    # @return a ListNode
    ___ swapPairs  head
        __ head __ N.. o. head.next __ N..
            r.. head
        ____:
            t = head.next
            head.next = swapPairs(t.next)
            t.next = head
            r.. t
