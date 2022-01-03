'''
Created on Nov 8, 2017

@author: MT
'''
# Definition for singly-linked list.
c_ ListNode(object):
    ___ - , val, nextNode_ N..
        val = val
        next = nextNode

c_ Solution(object):
    ___ addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        prev = dummy
        carry = 0
        w.... l1 a.. l2:
            tmpVal = l1.val+l2.val+carry
            __ tmpVal >= 10:
                tmpVal -= 10
                carry = 1
            ____:
                carry = 0
            prev.next = ListNode(tmpVal)
            l1 = l1.next
            l2 = l2.next
            prev = prev.next
        w.... l1:
            tmpVal = l1.val+carry
            __ tmpVal >= 10:
                tmpVal -= 10
                carry = 1
            ____:
                carry = 0
            prev.next = ListNode(tmpVal)
            l1 = l1.next
            prev = prev.next
        w.... l2:
            tmpVal = l2.val+carry
            __ tmpVal >= 10:
                tmpVal -= 10
                carry = 1
            ____:
                carry = 0
            prev.next = ListNode(tmpVal)
            l2 = l2.next
            prev = prev.next
        __ carry:
            prev.next = ListNode(1)
        r.. dummy.next
