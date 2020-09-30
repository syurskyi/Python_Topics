'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x, nextNode=None
        self.val = x
        self.next = nextNode

class Solution(object
    ___ insertionSortList(self, head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        w___ head:
            node = dummy
            w___ node.next and node.next.val < head.val:
                node = node.next
            tmp = head.next
            head.next = node.next
            node.next = head
            head = tmp
        r_ dummy.next
    
    ___ test(self
        testCases = [
            ListNode(3, ListNode(2, ListNode(5, ListNode(-1)))),
            ListNode(2, ListNode(1, ListNode(-3))),
        ]
        ___ head __ testCases:
            node = self.insertionSortList(head)
            w___ node:
                print('%s, ' % node.val, end='')
                node = node.next
            print()
            print('-='*20+'-')

__  -n __ '__main__':
    Solution().test()