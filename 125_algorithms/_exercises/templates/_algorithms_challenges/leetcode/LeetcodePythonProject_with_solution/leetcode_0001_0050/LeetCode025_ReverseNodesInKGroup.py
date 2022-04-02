'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x, nextNode_ N..
        val = x
        next = nextNode

c_ Solution(o..
    ___ reverseKGroup  head, k
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
                node = reverse(prev, node)
                prev = node
            count += 1
            node = node.next
        r.. dummy.next
    
    ___ reverse  prev, tail
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
