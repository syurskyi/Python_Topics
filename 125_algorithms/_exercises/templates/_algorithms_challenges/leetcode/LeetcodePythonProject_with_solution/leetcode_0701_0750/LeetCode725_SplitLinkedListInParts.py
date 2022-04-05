'''
Created on Feb 21, 2018

@author: tongq
'''
# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x, nextNode_ N..
        val = x
        next = nextNode

c_ Solution(o..
    ___ splitListToParts  root, k
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res    # list
        length = 0
        head = root
        w.... head:
            head = head.next
            length += 1
        length0 = length//k
        count0 = length-length0*k
        lengths = [length0]*k
        ___ i __ r..(count0
            lengths[i] += 1
        head = root
        prev = ListNode(-1)
        prev.next = head
        prevHead = head
        i = 0
        print('lengths: %s' % lengths)
        print('length: %s' % length)
        print('count0: %s' % count0)
        w.... head:
            __ lengths[i] __ 0:
                prev.next = N..
                i += 1
                res.a..(prevHead)
                prevHead = head
            lengths[i] -_ 1
            prev = head
            head = head.next
        res.a..(prevHead)
        ___ _ __ r..(i+1, k
            res.a..(N..)
        r.. res
    
    ___ test
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
            res = splitListToParts(head, k)
            print('res: %s' % res)

__ _____ __ _____
    Solution().test()
