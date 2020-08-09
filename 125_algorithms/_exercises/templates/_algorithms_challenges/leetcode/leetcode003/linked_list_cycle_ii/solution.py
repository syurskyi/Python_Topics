# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    ___ detectCycle(self, head
        __ head is None or head.next is None:
            r_ None
        slow = head
        fast = head
        w___ fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            __ fast __ slow:
                break
        # No cycle
        __ fast is None or fast.next is None:
            r_ None
        # Has a cycle, put `slow` back to head
        slow = head
        w___ True:
            __ fast __ slow:
                break
            slow = slow.next
            fast = fast.next
        r_ slow
