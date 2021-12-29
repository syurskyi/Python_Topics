'''
Created on Mar 18, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = N..

class Solution(object):
    ___ oddEvenList(self, head):
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