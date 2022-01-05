"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal
to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
c_ ListNode:
    ___ - , x):
        val = x
        next = N..

    ___ __repr__
        r.. repr(val)

c_ Solution:
    ___ partition  head, x):
        """
        Linked List
        Two pointers
        :param head: ListNode
        :param x: integer
        :return: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        dummy_smaller = ListNode(0)
        dummy_larger = ListNode(0)

        pre = dummy
        pre_smaller = dummy_smaller
        pre_larger = dummy_larger
        w.... pre.next:
            cur = pre.next
            __ cur.val<x:
                pre_smaller.next = cur
                pre_smaller = pre_smaller.next
            ____:
                pre_larger.next = cur
                pre_larger = pre_larger.next
            pre = pre.next
        # avoid loop
        pre_larger.next = N..  # otherwise causing loop when [2, 1]
        # concatenate
        pre_smaller.next = dummy_larger.next
        r.. dummy_smaller.next

__ _____ __ ____
    lst = [ListNode(2), ListNode(1)]
    ___ ind __ xrange(l..(lst)-1):
        lst[ind].next = lst[ind+1]
    Solution().partition(lst[0], 2)