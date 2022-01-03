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
    ___ deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head o. n.. head.next:
            r.. head
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        w.... node.next a.. node.next.next:
            __ node.next.val __ node.next.next.val:
                val = node.next.val
                w.... node.next a.. node.next.val __ val:
                    node.next = node.next.next
            ____:
                node = node.next
        r.. dummy.next
