"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(object):
    ___ hasCycle  head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        w.... fast __ n.. N.. a.. fast.next __ n.. N..
            slow = slow.next
            fast = fast.next.next
            __ slow __ fast:
                r.. T..
        r.. F..
