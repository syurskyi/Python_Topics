'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, val, nextNode_ N..
        self.val = val
        self.next = nextNode

class Solution(object):
    ___ mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        prev = dummy
        while l1 and l2:
            __ l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        __ l1:
            prev.next = l1
        __ l2:
            prev.next = l2
        return dummy.next
