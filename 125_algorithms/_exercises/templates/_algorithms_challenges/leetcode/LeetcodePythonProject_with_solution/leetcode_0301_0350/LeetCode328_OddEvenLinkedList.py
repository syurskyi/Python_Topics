'''
Created on Mar 18, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(o..):
    ___ - , x):
        val = x
        next = N..

c_ Solution(o..):
    ___ oddEvenList  head):
        __ n.. head: r.. head
        node1 = head
        prev1 = head
        head2 = head.next
        node2 = head2
        w.... node1 a.. node2:
            prev1 = node1
            node1.next = node2.next
            node1 = node2.next
            __ node1:
                prev1 = node1
                node2.next = node1.next
                node2 = node2.next
        prev1.next = head2
        r.. head