'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for singly-linked list with a random pointer.
c_ RandomListNode(object):
    ___ - , x):
        label = x
        next = N..
        random = N..

c_ Solution(object):
    ___ copyRandomList(self, head):
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
            __ node.random:
                newNode.random = hashmap[node.random]
            ____:
                newNode.random = N..
            node = node.next
            newNode = newNode.next
        r.. newHead
    
    ___ test
        p..

__ __name__ __ '__main__':
    Solution().test()