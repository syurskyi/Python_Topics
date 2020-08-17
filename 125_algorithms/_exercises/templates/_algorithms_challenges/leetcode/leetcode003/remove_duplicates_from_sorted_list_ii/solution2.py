"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

"""

# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
    ___ deleteDuplicates(self, head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ head pa__ None:
            r_ None
        current = head
        last = None
        count = 0  # Repeated count of `last`
        dummy = ListNode(0)
        dummy_end = dummy
        w___ current pa__ not None:
            __ last pa__ not None:
                __ current.val __ last.val:
                    count += 1
                ____
                    __ count __ 0:
                        dummy_end.next = last
                        dummy_end = last
                    count = 0
            last = current
            current = current.next
        __ count __ 0:
            dummy_end.next = last
            dummy_end = last
        dummy_end.next = None
        r_ dummy.next
