'''
Created on Feb 18, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(object):
    ___ - , x):
        val = x
        next = N..

c_ Solution(object):
    ___ removeElements  head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        node = dummy.next
        w.... node:
            __ node.val __ val:
                prev.next = node.next
            ____:
                prev = node
            node = node.next
        r.. dummy.next
