'''
Created on Feb 25, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x
        self.val = x
        self.next = None

class Solution(object
    ___ isPalindrome(self, head
        """
        :type head: ListNode
        :rtype: bool
        """
        __ not head or not head.next:
            r_ True
        node1 = head
        node2 = head
        w___ node2 and node2.next:
            node1 = node1.next
            node2 = node2.next
            __ node2.next:
                node2 = node2.next
        mid = node1
        p1 = mid
        p2 = mid.next
        p1.next = None
        w___ p1 and p2:
            nextNode = p2.next
            p2.next = p1
            p1 = p2
            p2 = nextNode
        node1 = head
        node2 = p1
        w___ node1 and node2:
            __ node1.val != node2.val:
                r_ False
            node1 = node1.next
            node2 = node2.next
        r_ True
