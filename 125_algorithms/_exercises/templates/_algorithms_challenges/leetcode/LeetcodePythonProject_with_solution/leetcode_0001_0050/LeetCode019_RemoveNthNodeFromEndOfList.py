'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, val, nextNode_ N..
        self.val = val
        self.next = nextNode

class Solution(object):
    ___ removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        ___ _ __ r..(n):
            fast = fast.next
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        node = head
        while fast:
            prev = node
            node = node.next
            fast = fast.next
        prev.next = node.next
        r.. dummy.next
