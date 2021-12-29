# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    ___ detectCycle(self, head):
        __ head __ N.. o. head.next __ N..
            r.. N..
        slow = head
        fast = head
        while fast __ n.. N.. and fast.next __ n.. N..
            slow = slow.next
            fast = fast.next.next
            __ fast __ slow:
                break
        # No cycle
        __ fast __ N.. o. fast.next __ N..
            r.. N..
        # Has a cycle, put `slow` back to head
        slow = head
        while True:
            __ fast __ slow:
                break
            slow = slow.next
            fast = fast.next
        r.. slow
