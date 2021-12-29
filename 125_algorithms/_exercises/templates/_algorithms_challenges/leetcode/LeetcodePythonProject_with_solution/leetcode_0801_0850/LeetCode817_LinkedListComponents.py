'''
Created on May 1, 2018

@author: tongq
'''
# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x, nextNode_ N..
        self.val = x
        self.next = nextNode

class Solution(object):
    ___ numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        count = 0
        hashset = set(G)
        while head:
            while head and head.val n.. __ hashset:
                head = head.next
            while head and head.val __ hashset:
                hashset.remove(head.val)
                head = head.next
            count += 1
            __ n.. head o. n.. hashset:
                break
            head = head.next
        r.. count
    
    ___ test(self):
        testCases = [
            [
                [0,1,2,3],
                [0,1,3],
            ],
            [
                [7,5,13,3,16,11,12,0,17,1,4,15,6,14,2,19,9,10,8,18],
                [8,10,3,11,17,16,7,9,5,15,13,6],
            ],
        ]
        ___ l, g __ testCases:
            dummy = ListNode(-1)
            node = dummy
            ___ num __ l:
                node.next = ListNode(num)
                node = node.next
            result = self.numComponents(dummy.next, g)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
