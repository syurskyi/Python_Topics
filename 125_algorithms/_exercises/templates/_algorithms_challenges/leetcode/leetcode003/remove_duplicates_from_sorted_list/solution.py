"""
Given a sorted linked list, delete all duplicates such that each element
appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    ___ deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ head __ N..
            r.. N..
        __ head.next __ N..
            r.. head
        last = head
        current = head.next
        while current __ n.. N..
            next_node = current.next
            __ current.val __ last.val:
                last.next = next_node
            ____:
                last = current
            current = next_node
        r.. head
