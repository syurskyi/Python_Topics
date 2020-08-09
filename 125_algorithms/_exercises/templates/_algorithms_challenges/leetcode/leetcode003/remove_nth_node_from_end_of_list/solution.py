# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    ___ removeNthFromEnd(self, head, n
        __ head is None:
            r_ None
        ____ n __ 0:
            r_ head
        ____
            q = p = pp = head  # `pp` is the node preceding `p`
            w___ q is not None:
                __ n <= 0:
                    pp = p
                    p = p.next
                q = q.next
                n -= 1
            # Remove the head node
            __ pp is p:
                head = pp.next
            ____
                pp.next = p.next
                # Free p
            r_ head
