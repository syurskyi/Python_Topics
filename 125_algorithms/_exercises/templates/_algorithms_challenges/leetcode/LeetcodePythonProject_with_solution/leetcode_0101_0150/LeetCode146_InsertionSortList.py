'''
Created on Feb 9, 2017

@author: MT
'''

# Definition for singly-linked list.
c_ ListNode(object):
    ___ - , x, nextNode_ N..
        val = x
        next = nextNode

c_ Solution(object):
    ___ insertionSortList  head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        w.... head:
            node = dummy
            w.... node.next a.. node.next.val < head.val:
                node = node.next
            tmp = head.next
            head.next = node.next
            node.next = head
            head = tmp
        r.. dummy.next
    
    ___ test
        testCases = [
            ListNode(3, ListNode(2, ListNode(5, ListNode(-1)))),
            ListNode(2, ListNode(1, ListNode(-3))),
        ]
        ___ head __ testCases:
            node = insertionSortList(head)
            w.... node:
                print('%s, ' % node.val, end='')
                node = node.next
            print()
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()