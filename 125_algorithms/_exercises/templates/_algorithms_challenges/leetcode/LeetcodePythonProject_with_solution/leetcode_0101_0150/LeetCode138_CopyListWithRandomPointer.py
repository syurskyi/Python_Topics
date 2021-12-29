'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    ___ __init__(self, x):
        self.label = x
        self.next = N..
        self.random = N..

class Solution(object):
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
        while node:
            tmp = RandomListNode(node.label)
            hashmap[node] = tmp
            newNode.next = tmp
            newNode = newNode.next
            node = node.next
        node = head
        newNode = newHead
        while node:
            __ node.random:
                newNode.random = hashmap[node.random]
            ____:
                newNode.random = N..
            node = node.next
            newNode = newNode.next
        r.. newHead
    
    ___ test(self):
        pass

__ __name__ __ '__main__':
    Solution().test()