'''
Created on Jan 24, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x
        self.val = x
        self.next = None

class Solution(object
    ___ deleteDuplicates(self, head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ not head or not head.next:
            r_ head
        node = head
        w___ node.next:
            __ node.next.val __ node.val:
                val = node.val
                w___ node.next and node.next.val __ val:
                    node.next = node.next.next
            node = node.next
        r_ head
