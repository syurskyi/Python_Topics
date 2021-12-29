'''
Created on Feb 10, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x):
        self.val = x
        self.next = N..

class Solution(object):
    ___ sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r.. self.helper(head)
    
    ___ helper(self, node):
        __ n.. node o. n.. node.next:
            r.. node
        prev = ListNode(-1)
        node1 = node
        prev.next = node1
        node2 = node
        while node2:
            node2 = node2.next
            __ n.. node2: break
            prev = node1
            node1 = node1.next
            node2 = node2.next
        prev.next = N..
        mid = node1
        result1 = self.helper(node)
        result2 = self.helper(mid)
        result = self.merge(result1, result2)
        r.. result
    
    ___ merge(self, node1, node2):
        __ n.. node1:
            r.. node2
        __ n.. node2:
            r.. node1
        __ node1.val > node2.val:
            node = node2
            node2 = node2.next
        ____:
            node = node1
            node1 = node1.next
        head = node
        while node:
            __ n.. node1 and n.. node2:
                r.. head
            ____ n.. node1 and node2:
                node.next = node2
                node = node.next
                node2 = node2.next
            ____ node1 and n.. node2:
                node.next = node1
                node = node.next
                node1 = node1.next
            ____:
                __ node1.val < node2.val:
                    node.next = node1
                    node = node.next
                    node1 = node1.next
                ____:
                    node.next = node2
                    node = node.next
                    node2 = node2.next
        r.. head
    