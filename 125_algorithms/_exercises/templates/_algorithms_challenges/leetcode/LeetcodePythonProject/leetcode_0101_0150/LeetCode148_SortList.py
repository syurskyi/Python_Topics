'''
Created on Feb 10, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x
        self.val = x
        self.next = None

class Solution(object
    ___ sortList(self, head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r_ self.helper(head)
    
    ___ helper(self, node
        __ not node or not node.next:
            r_ node
        prev = ListNode(-1)
        node1 = node
        prev.next = node1
        node2 = node
        w___ node2:
            node2 = node2.next
            __ not node2: break
            prev = node1
            node1 = node1.next
            node2 = node2.next
        prev.next = None
        mid = node1
        result1 = self.helper(node)
        result2 = self.helper(mid)
        result = self.merge(result1, result2)
        r_ result
    
    ___ merge(self, node1, node2
        __ not node1:
            r_ node2
        __ not node2:
            r_ node1
        __ node1.val > node2.val:
            node = node2
            node2 = node2.next
        ____
            node = node1
            node1 = node1.next
        head = node
        w___ node:
            __ not node1 and not node2:
                r_ head
            ____ not node1 and node2:
                node.next = node2
                node = node.next
                node2 = node2.next
            ____ node1 and not node2:
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
        r_ head
    