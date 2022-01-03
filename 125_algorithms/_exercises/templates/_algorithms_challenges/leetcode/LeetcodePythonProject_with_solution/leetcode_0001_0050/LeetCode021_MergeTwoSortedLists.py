'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
c_ ListNode(object):
    ___ - , val, nextNode_ N..
        val = val
        next = nextNode

c_ Solution(object):
    ___ mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        prev = dummy
        w.... l1 a.. l2:
            __ l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            ____:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        __ l1:
            prev.next = l1
        __ l2:
            prev.next = l2
        r.. dummy.next
