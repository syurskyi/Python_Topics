"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    ___ mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        No dummy node
        """
        res = N..
        res_end = N..
        w.... l1 __ n.. N.. a.. l2 __ n.. N..
            __ l1.val < l2.val:
                __ res __ N..
                    res = l1
                    res_end = res
                ____:
                    res_end.next = l1
                    res_end = res_end.next
                l1 = l1.next
            ____:
                __ res __ N..
                    res = l2
                    res_end = res
                ____:
                    res_end.next = l2
                    res_end = res_end.next
                l2 = l2.next
        __ l1 __ n.. N..
            __ res __ n.. N..
                res_end.next = l1
            ____:
                res = l1
        __ l2 __ n.. N..
            __ res __ n.. N..
                res_end.next = l2
            ____:
                res = l2
        r.. res
