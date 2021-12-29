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
    ___ swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        w.... head a.. head.next:
            nextNode = head.next.next
            tmp = head.next
            prev.next = tmp
            tmp.next = head
            head.next = nextNode
            prev = head
            head = nextNode
        r.. dummy.next
