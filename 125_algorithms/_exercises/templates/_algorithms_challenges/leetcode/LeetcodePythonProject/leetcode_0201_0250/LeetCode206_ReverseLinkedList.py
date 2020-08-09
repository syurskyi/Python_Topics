'''
Created on Feb 18, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x, nextNode=None
        self.val = x
        self.next = nextNode

class Solution(object
    ___ reverseList(self, head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ not head or not head.next: r_ head
        p1 = head
        p2 = head.next
        p1.next = None
        w___ p1 and p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        r_ p1
    
    ___ reverseListRecursive(self, head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        __ not head or not head.next: r_ head
        second = head.next
        head.next = None
        rest = self.reverseListRecursive(second)
        second.next = head
        r_ rest
    
    ___ test(self
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        node = head
        w___ node:
            print('%s => ' % node.val, end='')
            node = node.next
        node = self.reverseList(head)
        print()
        newHead = node
        w___ node:
            print('%s => ' % node.val, end='')
            node = node.next
        print()
        node = self.reverseListRecursive(newHead)
        w___ node:
            print('%s => ' % node.val, end='')
            node = node.next
        print()

__ __name__ __ '__main__':
    Solution().test()

        