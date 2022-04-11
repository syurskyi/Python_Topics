"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the
list or null.

Return a deep copy of the list.
"""
__author__ 'Danyang'
# Definition for singly-linked list with a random pointer.
c_ RandomListNode:
    ___ - , x
        label x
        next N..
        r__ N..

c_ Solution:
    ___ copyRandomList  head
        """
        Algorithm:

        Duplicate the node in the list
        Split the list into two

        A->B->C

        A->A'->B->B'->C->C'

        A->B->C
        A'->B'->C'

        :param head: RandomListNode
        :return: RandomListNode
        """
        # duplicate
        dummy RandomListNode(0)
        dummy.next head

        pre dummy
        w.... pre.next:
            cur pre.next
            cur_copy RandomListNode(cur.label)

            temp cur.next
            cur.next cur_copy
            cur_copy.next temp

            pre pre.next.next

        # copy random
        pre dummy
        w.... pre.next:
            cur pre.next

            __ cur.r__:
                cur.next.r__ cur.r__.next  # for duplicated node. NEXT IS RANDOM

            pre pre.next.next

        # split
        pre dummy
        head_copy pre.next.next __ pre.next ____ N..
        w.... pre.next:
            cur pre.next
            cur_copy cur.next

            cur.next cur_copy.next
            __ cur_copy.next:
                cur_copy.next cur_copy.next.next

            pre pre.next


        r.. head_copy