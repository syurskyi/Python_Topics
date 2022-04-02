'''
Created on Feb 25, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x
        val = x
        next = N..

c_ Solution(o..
    ___ isPalindrome  head
        """
        :type head: ListNode
        :rtype: bool
        """
        __ n.. head o. n.. head.next:
            r.. T..
        node1 = head
        node2 = head
        w.... node2 a.. node2.next:
            node1 = node1.next
            node2 = node2.next
            __ node2.next:
                node2 = node2.next
        mid = node1
        p1 = mid
        p2 = mid.next
        p1.next = N..
        w.... p1 a.. p2:
            nextNode = p2.next
            p2.next = p1
            p1 = p2
            p2 = nextNode
        node1 = head
        node2 = p1
        w.... node1 a.. node2:
            __ node1.val != node2.val:
                r.. F..
            node1 = node1.next
            node2 = node2.next
        r.. T..
