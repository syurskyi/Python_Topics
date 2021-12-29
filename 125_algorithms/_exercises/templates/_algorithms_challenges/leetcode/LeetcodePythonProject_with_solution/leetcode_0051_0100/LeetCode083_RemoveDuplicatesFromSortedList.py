'''
Created on Jan 24, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = N..

class Solution(object):
    ___ deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head o. n.. head.next:
            r.. head
        node = head
        while node.next:
            __ node.next.val __ node.val:
                val = node.val
                while node.next and node.next.val __ val:
                    node.next = node.next.next
            node = node.next
        r.. head
