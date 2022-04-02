'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , val, nextNode_ N..
        val = val
        next = nextNode

c_ Solution(o..
    ___ swapPairs  head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        w.... head a.. head.next:
            nextNode = head.next.next
            tmp = head.next
            prev.next = tmp
            tmp.next = head
            head.next = nextNode
            prev = head
            head = nextNode
        r.. dummy.next
