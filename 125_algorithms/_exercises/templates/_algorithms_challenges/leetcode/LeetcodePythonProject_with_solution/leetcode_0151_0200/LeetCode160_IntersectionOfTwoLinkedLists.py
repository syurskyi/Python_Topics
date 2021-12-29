'''
Created on May 22, 2018

@author: tongq
'''
# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x, nextNode):
        self.val = x
        self.next = nextNode

class Solution(object):
    ___ getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        __ n.. lenA o. n.. lenB: r.. N..
        __ lenA < lenB:
            headA, headB = headB, headA
        diff = abs(lenA-lenB)
        w.... diff a.. headA:
            headA = headA.next
            diff -= 1
        w.... headA a.. headB:
            __ headA __ headB:
                r.. headA
            headA = headA.next
            headB = headB.next
        r.. N..
    
    ___ getLength(self, head):
        length = 0
        w.... head:
            head = head.next
            length += 1
        r.. length
