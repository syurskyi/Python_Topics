'''
Created on Feb 21, 2018

@author: tongq
'''
# Definition for singly-linked list.
class ListNode(object):
    ___ __init__(self, x, nextNode_ N..
        self.val = x
        self.next = nextNode

class Solution(object):
    ___ splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res    # list
        length = 0
        head = root
        while head:
            head = head.next
            length += 1
        length0 = length//k
        count0 = length-length0*k
        lengths = [length0]*k
        ___ i __ r..(count0):
            lengths[i] += 1
        head = root
        prev = ListNode(-1)
        prev.next = head
        prevHead = head
        i = 0
        print('lengths: %s' % lengths)
        print('length: %s' % length)
        print('count0: %s' % count0)
        while head:
            __ lengths[i] __ 0:
                prev.next = N..
                i += 1
                res.a..(prevHead)
                prevHead = head
            lengths[i] -= 1
            prev = head
            head = head.next
        res.a..(prevHead)
        ___ _ __ r..(i+1, k):
            res.a..(N..)
        r.. res
    
    ___ test(self):
        testCases = [
            [
                ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
                5,
            ],
            [
                ListNode(1, ListNode(2, ListNode(3))),
                5,
            ],
        ]
        ___ head, k __ testCases:
            res = self.splitListToParts(head, k)
            print('res: %s' % res)

__ __name__ __ '__main__':
    Solution().test()
