'''
Created on Jan 26, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    ___ partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        __ not head:
            return head
        aHead, bHead = ListNode(0), ListNode(0)
        aTail, bTail = aHead, bHead
        while head:
            __ head.val < x:
                aTail.next = head
                aTail = aTail.next
            else:
                bTail.next = head
                bTail = bTail.next
            head = head.next
        aTail.next = bHead.next
        bTail.next = None
        return aHead.next
    
    ___ test(self):
        pass
