'''
Created on Feb 25, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = N..

class Solution(object):
    ___ isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        __ n.. head o. n.. head.next:
            r.. True
        node1 = head
        node2 = head
        w.... node2 a.. node2.next:
            node1 = node1.next
            node2 = node2.next
            __ node2.next:
                node2 = node2.next
        mid = node1
        p1 = mid
        p2 = mid.next
        p1.next = N..
        w.... p1 a.. p2:
            nextNode = p2.next
            p2.next = p1
            p1 = p2
            p2 = nextNode
        node1 = head
        node2 = p1
        w.... node1 a.. node2:
            __ node1.val != node2.val:
                r.. False
            node1 = node1.next
            node2 = node2.next
        r.. True
