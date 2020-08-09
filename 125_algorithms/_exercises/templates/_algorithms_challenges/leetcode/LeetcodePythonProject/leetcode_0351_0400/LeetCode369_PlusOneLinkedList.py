'''
Created on Mar 29, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x
        self.val = x
        self.next = None

class Solution(object
    ___ plusOne(self, head
        __ not head: r_ ListNode(1)
        newHead = self.reverse(head)
        carry = 1
        node = newHead
        tail = node
        w___ node and carry:
            val = node.val + carry
            __ val >= 10:
                val -= 10
                carry = 1
            ____
                carry = 0
            node.val = val
            tail = node
            node = node.next
        __ carry:
            tail.next = ListNode(1)
        r_ self.reverse(newHead)
    
    ___ reverse(self, head
        p1 = head
        p2 = p1.next
        p1.next = None
        w___ p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        r_ p1
    