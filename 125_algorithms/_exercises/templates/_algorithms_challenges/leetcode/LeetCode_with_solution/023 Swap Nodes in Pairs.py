"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be
changed.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x):
        val = x
        next = N..

c_ Solution:
    ___ swapPairs  head):
        """
        Linked List
        :param head: ListNode
        :return: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        w.... pre.next a.. pre.next.next:
            node1 = pre.next
            node2 = pre.next.next

            # temp = node2.next
            # pre.next = node2
            # node2.next = node1
            # node1.next = temp

            pre.next, node1.next, node2.next = node2, node2.next, node1

            pre = pre.next.next

        r.. dummy.next