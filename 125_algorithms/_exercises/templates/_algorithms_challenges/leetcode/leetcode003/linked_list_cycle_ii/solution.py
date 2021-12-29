# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    ___ detectCycle(self, head):
        __ head __ None or head.next __ None:
            return None
        slow = head
        fast = head
        while fast __ not None and fast.next __ not None:
            slow = slow.next
            fast = fast.next.next
            __ fast == slow:
                break
        # No cycle
        __ fast __ None or fast.next __ None:
            return None
        # Has a cycle, put `slow` back to head
        slow = head
        while True:
            __ fast == slow:
                break
            slow = slow.next
            fast = fast.next
        return slow
