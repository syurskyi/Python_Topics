'''
Created on Feb 18, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(o..):
    ___ - , x, nextNode_ N..
        val = x
        next = nextNode

c_ Solution(o..):
    ___ reverseList  head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head o. n.. head.next: r.. head
        p1 = head
        p2 = head.next
        p1.next = N..
        w.... p1 a.. p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        r.. p1
    
    ___ reverseListRecursive  head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ n.. head o. n.. head.next: r.. head
        second = head.next
        head.next = N..
        rest = reverseListRecursive(second)
        second.next = head
        r.. rest
    
    ___ test
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        node = head
        w.... node:
            print('%s => ' % node.val, end='')
            node = node.next
        node = reverseList(head)
        print()
        newHead = node
        w.... node:
            print('%s => ' % node.val, end='')
            node = node.next
        print()
        node = reverseListRecursive(newHead)
        w.... node:
            print('%s => ' % node.val, end='')
            node = node.next
        print()

__ _____ __ _____
    Solution().test()

        