"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the
original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
__author__ 'Danyang'
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x
        val x
        next N..

c_ Solution:
    ___ deleteDuplicates  head
        """
        Two pointers
        :param head: ListNode
        :return: ListNode
        """
        dummy ? 0
        dummy.next head

        pre dummy
        w.... pre.next:
            cur pre.next
            __ cur.next a.. cur.next.val__cur.val:  # duplicated
                # find the next non_duplicate
                next_non_duplicate cur.next
                w.... next_non_duplicate a.. cur.val__next_non_duplicate.val:
                    next_non_duplicate next_non_duplicate.next

                # remove all duplicated nodes 
                pre.next next_non_duplicate

            ____
                pre pre.next

        r.. dummy.next




