'''
Created on Jan 28, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x, nextNode=None
        self.val = x
        self.next = nextNode

class Solution(object
    ___ reverseBetween(self, head, m, n
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        __ m >= n or not head:
            r_ head
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        for _ in range(1, m
            __ not head:
                r_ None
            head = head.next
        prevNode = head
        mNode = head.next
        nNode, postnNode = mNode, mNode.next
        for _ in range(m, n
            __ not postnNode:
                r_ None
            tmp = postnNode.next
            postnNode.next = nNode
            nNode = postnNode
            postnNode = tmp
        mNode.next = postnNode
        prevNode.next = nNode
        r_ dummy.next
    
    ___ test(self
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        node = self.reverseBetween(head, 2, 4)
        w___ node:
            print(node.val)
            node = node.next
        print

___ main(
    Solution().test()

__ __name__ __ '__main__':
    main()