'''
Created on Jan 24, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(object):
    ___ - , x):
        val = x
        next = N..

c_ Solution(object):
    ___ deleteDuplicates  head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head o. n.. head.next:
            r.. head
        node = head
        w.... node.next:
            __ node.next.val __ node.val:
                val = node.val
                w.... node.next a.. node.next.val __ val:
                    node.next = node.next.next
            node = node.next
        r.. head
