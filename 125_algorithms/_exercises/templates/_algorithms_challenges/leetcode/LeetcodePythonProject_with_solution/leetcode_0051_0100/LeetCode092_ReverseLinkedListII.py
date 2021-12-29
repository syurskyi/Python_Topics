'''
Created on Jan 28, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x, nextNode_ N..
        self.val = x
        self.next = nextNode

class Solution(object):
    ___ reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        __ m >= n o. n.. head:
            r.. head
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        ___ _ __ r..(1, m):
            __ n.. head:
                r.. N..
            head = head.next
        prevNode = head
        mNode = head.next
        nNode, postnNode = mNode, mNode.next
        ___ _ __ r..(m, n):
            __ n.. postnNode:
                r.. N..
            tmp = postnNode.next
            postnNode.next = nNode
            nNode = postnNode
            postnNode = tmp
        mNode.next = postnNode
        prevNode.next = nNode
        r.. dummy.next
    
    ___ test(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        node = self.reverseBetween(head, 2, 4)
        w.... node:
            print(node.val)
            node = node.next
        print

___ main():
    Solution().test()

__ __name__ __ '__main__':
    main()