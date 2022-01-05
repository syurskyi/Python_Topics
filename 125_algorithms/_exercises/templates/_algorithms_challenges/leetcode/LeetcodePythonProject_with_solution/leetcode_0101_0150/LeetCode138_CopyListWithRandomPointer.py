'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for singly-linked list with a random pointer.
c_ RandomListNode(o..):
    ___ - , x):
        label = x
        next = N..
        r__ = N..

c_ Solution(o..):
    ___ copyRandomList  head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        __ n.. head: r.. head
        newHead = RandomListNode(head.label)
        newNode = newHead
        hashmap = {head: newHead}
        node = head.next
        w.... node:
            tmp = RandomListNode(node.label)
            hashmap[node] = tmp
            newNode.next = tmp
            newNode = newNode.next
            node = node.next
        node = head
        newNode = newHead
        w.... node:
            __ node.r__:
                newNode.r__ = hashmap[node.r__]
            ____:
                newNode.r__ = N..
            node = node.next
            newNode = newNode.next
        r.. newHead
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()