'''
Created on May 22, 2018

@author: tongq
'''
# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x, nextNode
        val = x
        next = nextNode

c_ Solution(o..
    ___ getIntersectionNode  headA, headB
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = getLength(headA)
        lenB = getLength(headB)
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
    
    ___ getLength  head
        length = 0
        w.... head:
            head = head.next
            length += 1
        r.. length
