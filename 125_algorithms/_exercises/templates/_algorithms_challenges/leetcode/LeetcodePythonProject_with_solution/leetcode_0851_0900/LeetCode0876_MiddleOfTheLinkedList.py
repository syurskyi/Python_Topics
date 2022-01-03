'''
Created on Oct 8, 2019

@author: tongq
'''
# Definition for singly-linked list.
c_ ListNode(object):
    ___ - , x):
        val = x
        next = N..

c_ Solution(object):
    ___ middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head: r.. N..
        count = 0
        node = head
        w.... node:
            count += 1
            node = node.next
        count >>= 1
        node = head
        ___ _ __ r..(count):
            node = node.next
        r.. node
