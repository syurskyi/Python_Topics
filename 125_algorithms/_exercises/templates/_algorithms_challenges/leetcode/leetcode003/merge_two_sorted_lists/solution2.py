"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
c_ ListNode(o..):
    ___ - , x):
        val = x
        next = N..

c_ Solution(o..):
    ___ mergeTwoLists  l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Dummy node
        """
        dummy = ListNode(0)
        dummy_end = dummy

        w.... l1 __ n.. N.. a.. l2 __ n.. N..
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
