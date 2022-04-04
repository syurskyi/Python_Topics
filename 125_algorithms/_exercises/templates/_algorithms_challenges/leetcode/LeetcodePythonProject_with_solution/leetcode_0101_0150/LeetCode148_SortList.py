'''
Created on Feb 10, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x
        val = x
        next = N..

c_ Solution(o..
    ___ sortList  head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r.. helper(head)
    
    ___ helper  node
        __ n.. node o. n.. node.next:
            r.. node
        prev = ListNode(-1)
        node1 = node
        prev.next = node1
        node2 = node
        w.... node2:
            node2 = node2.next
            __ n.. node2: _____
            prev = node1
            node1 = node1.next
            node2 = node2.next
        prev.next = N..
        mid = node1
        result1 = helper(node)
        result2 = helper(mid)
        result = merge(result1, result2)
        r.. result
    
    ___ merge  node1, node2
        __ n.. node1:
            r.. node2
        __ n.. node2:
            r.. node1
        __ node1.val > node2.val:
            node = node2
            node2 = node2.next
        ____
            node = node1
            node1 = node1.next
        head = node
        w.... node:
            __ n.. node1 a.. n.. node2:
                r.. head
            ____ n.. node1 a.. node2:
                node.next = node2
                node = node.next
                node2 = node2.next
            ____ node1 a.. n.. node2:
                node.next = node1
                node = node.next
                node1 = node1.next
            ____
                __ node1.val < node2.val:
                    node.next = node1
                    node = node.next
                    node1 = node1.next
                ____
                    node.next = node2
                    node = node.next
                    node2 = node2.next
        r.. head
    