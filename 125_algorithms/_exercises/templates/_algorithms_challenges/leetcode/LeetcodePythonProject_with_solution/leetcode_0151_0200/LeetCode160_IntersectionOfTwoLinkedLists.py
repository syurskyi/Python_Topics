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
        __ not lenA or not lenB: return None
        __ lenA < lenB:
            headA, headB = headB, headA
        diff = abs(lenA-lenB)
        while diff and headA:
            headA = headA.next
            diff -= 1
        while headA and headB:
            __ headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
    ___ getLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
