# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution:
    # @param head, a ListNode
    # @return a list node
    ___ detectCycle  head
        __ head __ N.. o. head.next __ N..
            r.. N..
        slow head
        fast head
        w.... fast __ n.. N.. a.. fast.next __ n.. N..
            slow slow.next
            fast fast.next.next
            __ fast __ slow:
                _____
        # No cycle
        __ fast __ N.. o. fast.next __ N..
            r.. N..
        # Has a cycle, put `slow` back to head
        slow head
        w... T...
            __ fast __ slow:
                _____
            slow slow.next
            fast fast.next
        r.. slow
