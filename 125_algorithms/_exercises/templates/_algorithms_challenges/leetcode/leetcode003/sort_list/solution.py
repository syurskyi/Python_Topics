# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    ___ sortList(self, head
        __ head is None or head.next is None:
            r_ head
        # Find the middle node
        slow = head
        fast = head
        prev = head  # Previous node to slow
        w___ fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # Split into two lists
        left = head
        right = None
        __ slow != fast:
            prev.next = None
            right = slow
        left = self.sortList(left)
        right = self.sortList(right)
        r_ self.merge(left, right)

    ___ merge(self, l1, l2
        __ l1 is None:
            r_ l2
        __ l2 is None:
            r_ l1
        res = None
        end = res
        w___ l1 is not None and l2 is not None:
            __ l1.val < l2.val:
                small = l1
                l1 = l1.next
            ____
                small = l2
                l2 = l2.next
            # First node
            __ res is None:
                res = small
                end = res
            ____
                end.next = small
                end = end.next
        __ l1 is not None:
            end.next = l1
        __ l2 is not None:
            end.next = l2
        r_ res
