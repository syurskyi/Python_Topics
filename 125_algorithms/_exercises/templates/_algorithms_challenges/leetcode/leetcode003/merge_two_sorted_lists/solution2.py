"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = N..

class Solution(object):
    ___ mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Dummy node
        """
        dummy = ListNode(0)
        dummy_end = dummy

        while l1 __ n.. N.. and l2 __ n.. N..
            __ l1.val < l2.val:
                dummy_end.next = l1
                l1 = l1.next
            ____:
                dummy_end.next = l2
                l2 = l2.next
            dummy_end = dummy_end.next
        __ l1 __ n.. N..
            dummy_end.next = l1
        ____:
            dummy_end.next = l2
        r.. dummy.next
