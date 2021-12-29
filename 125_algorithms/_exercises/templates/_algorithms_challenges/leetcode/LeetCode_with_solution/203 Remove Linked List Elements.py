"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
__author__ = 'Daniel'


class ListNode:
    ___ __init__(self, x):
        self.val = x
        self.next = N..


class Solution:
    ___ removeElements(self, head, val):
        """

        :param head:
        :param val:
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        w.... pre.next:
            cur = pre.next
            __ cur.val __ val:
                pre.next = cur.next
                continue

            pre = pre.next

        r.. dummy.next