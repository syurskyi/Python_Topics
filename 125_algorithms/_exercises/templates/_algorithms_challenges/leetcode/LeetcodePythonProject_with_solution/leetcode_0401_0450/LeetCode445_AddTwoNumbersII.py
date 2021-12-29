'''
Created on Apr 18, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = N..

class Solution(object):
    ___ addTwoNumbers(self, l1, l2):
        stack1    # list
        stack2    # list
        while l1:
            stack1.a..(l1.val)
            l1 = l1.next
        while l2:
            stack2.a..(l2.val)
            l2 = l2.next
        carry = 0
        nextNode = N..
        while stack1 and stack2:
            v1, v2 = stack1.pop(), stack2.pop()
            val = v1 + v2 + carry
            __ val >= 10:
                val -= 10
                carry = 1
            ____:
                carry = 0
            node = ListNode(val)
            node.next = nextNode
            nextNode = node
        __ stack2 and n.. stack1:
            stack1, stack2 = stack2, stack1
        while stack1:
            val = stack1.pop() + carry
            __ val >= 10:
                val -= 10
                carry = 1
            ____:
                carry = 0
            node = ListNode(val)
            node.next = nextNode
            nextNode = node
        __ carry:
            node = ListNode(1)
            node.next = nextNode
            nextNode = node
        r.. nextNode
