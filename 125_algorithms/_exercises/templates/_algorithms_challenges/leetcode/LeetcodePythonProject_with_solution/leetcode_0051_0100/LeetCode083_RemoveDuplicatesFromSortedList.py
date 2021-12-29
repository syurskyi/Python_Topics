'''
Created on Jan 24, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    ___ deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ not head or not head.next:
            return head
        node = head
        while node.next:
            __ node.next.val == node.val:
                val = node.val
                while node.next and node.next.val == val:
                    node.next = node.next.next
            node = node.next
        return head
