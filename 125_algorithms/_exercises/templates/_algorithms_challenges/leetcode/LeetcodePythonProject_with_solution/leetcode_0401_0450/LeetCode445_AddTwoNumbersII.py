'''
Created on Apr 18, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x
        val x
        next N..

c_ Solution(o..
    ___ addTwoNumbers  l1, l2
        stack1    # list
        stack2    # list
        w.... l1:
            stack1.a..(l1.val)
            l1 l1.next
        w.... l2:
            stack2.a..(l2.val)
            l2 l2.next
        carry 0
        nextNode N..
        w.... stack1 a.. stack2:
            v1, v2 stack1.p.. ), stack2.p.. )
            val v1 + v2 + carry
            __ val >_ 10:
                val -_ 10
                carry 1
            ____
                carry 0
            node ListNode(val)
            node.next nextNode
            nextNode node
        __ stack2 a.. n.. stack1:
            stack1, stack2 stack2, stack1
        w.... stack1:
            val stack1.p.. ) + carry
            __ val >_ 10:
                val -_ 10
                carry 1
            ____
                carry 0
            node ListNode(val)
            node.next nextNode
            nextNode node
        __ carry:
            node ListNode(1)
            node.next nextNode
            nextNode node
        r.. nextNode
