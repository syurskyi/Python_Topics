'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x, nextNode_ N..
        self.val = x
        self.next = nextNode

class Solution(object):
    ___ reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        __ k __ 1: r.. head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        count = 1
        node = head
        w.... node:
            __ count % k __ 0:
                node = self.reverse(prev, node)
                prev = node
            count += 1
            node = node.next
        r.. dummy.next
    
    ___ reverse(self, prev, tail):
        nextNode = tail.next
        p = prev.next
        res = p
        w.... p != nextNode:
            tmp = p.next
            p.next = prev.next
            prev.next = p
            p = tmp
        res.next = p
        r.. res
