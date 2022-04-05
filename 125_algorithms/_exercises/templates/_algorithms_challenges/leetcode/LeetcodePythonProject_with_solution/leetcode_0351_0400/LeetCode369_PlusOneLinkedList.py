'''
Created on Mar 29, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x
        val = x
        next = N..

c_ Solution(o..
    ___ plusOne  head
        __ n.. head: r.. ListNode(1)
        newHead = reverse(head)
        carry = 1
        node = newHead
        tail = node
        w.... node a.. carry:
            val = node.val + carry
            __ val >_ 10:
                val -_ 10
                carry = 1
            ____
                carry = 0
            node.val = val
            tail = node
            node = node.next
        __ carry:
            tail.next = ListNode(1)
        r.. reverse(newHead)
    
    ___ reverse  head
        p1 = head
        p2 = p1.next
        p1.next = N..
        w.... p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        r.. p1
    