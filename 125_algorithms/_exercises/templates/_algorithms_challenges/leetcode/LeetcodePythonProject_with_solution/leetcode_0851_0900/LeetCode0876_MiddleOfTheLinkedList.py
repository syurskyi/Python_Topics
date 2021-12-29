'''
Created on Oct 8, 2019

@author: tongq
'''
# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = N..

class Solution(object):
    ___ middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head: r.. N..
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        count >>= 1
        node = head
        ___ _ __ r..(count):
            node = node.next
        r.. node
