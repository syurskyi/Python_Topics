'''
Created on Jan 22, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x
        self.val = x
        self.next = None

class Solution(object
    ___ rotateRight(self, head, k
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        __ not head or not head.next or k __ 0:
            r_ head
        length = 0
        node = head
        w___ node:
            node = node.next
            length +=1
        node = head
        k = k % length
        __ k __ 0: r_ head
        prev = None
        count = 0
        w___ count < length-k:
            prev = node
            node = node.next
            count+=1
        tail = node
        w___ tail.next:
            tail = tail.next
        tail.next = head
        prev.next = None
        r_ node
    
    ___ test(self
        pass

__ __name__ __ '__main__':
    Solution().test()
