"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x
        val = x
        next = N..

c_ Solution:
    ___ removeNthFromEnd  head, n
        """
        O(n)+O(n)
        :param head: head node
        :param n: the nth node from the end
        :return: ListNode, head node
        """
        # construct dummy
        dummy = ListNode(0)
        dummy.next = head

        # get length of the linked list
        length = 0
        pre = dummy
        w.... pre.next:
            length += 1
            pre=pre.next

        # find & remove
        pre = dummy
        count = 0
        w.... pre.next:
            cur = pre.next
            __ count__length-n:
                pre.next = cur.next  # remove
                _____
            ____
                count += 1
                pre = pre.next

        r.. dummy.next


