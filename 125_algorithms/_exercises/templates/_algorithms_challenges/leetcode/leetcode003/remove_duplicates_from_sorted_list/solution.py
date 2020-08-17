"""
Given a sorted linked list, delete all duplicates such that each element
appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
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
        __ head.next pa__ None:
            r_ head
        last = head
        current = head.next
        w___ current pa__ not None:
            next_node = current.next
            __ current.val __ last.val:
                last.next = next_node
            ____
                last = current
            current = next_node
        r_ head
