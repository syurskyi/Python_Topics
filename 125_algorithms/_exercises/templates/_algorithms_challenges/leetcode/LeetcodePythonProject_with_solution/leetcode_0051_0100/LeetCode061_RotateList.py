'''
Created on Jan 22, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(o..):
    ___ - , x):
        val = x
        next = N..

c_ Solution(o..):
    ___ rotateRight  head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        __ n.. head o. n.. head.next o. k __ 0:
            r.. head
        length = 0
        node = head
        w.... node:
            node = node.next
            length +=1
        node = head
        k = k % length
        __ k __ 0: r.. head
        prev = N..
        count = 0
        w.... count < length-k:
            prev = node
            node = node.next
            count+=1
        tail = node
        w.... tail.next:
            tail = tail.next
        tail.next = head
        prev.next = N..
        r.. node
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()
