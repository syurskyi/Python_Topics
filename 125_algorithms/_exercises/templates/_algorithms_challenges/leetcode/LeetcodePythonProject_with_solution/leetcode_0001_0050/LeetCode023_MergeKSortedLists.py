'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , val, nextNode_ N..
        val val
        next nextNode

c_ Solution(o..
    ___ mergeKLists  lists
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        _______ h__
        heap    # list
        ___ l __ lists:
            w.... l:
                h__.heappush(heap, l.val)
                l l.next
        dummy ListNode(-1)
        prev dummy
        w.... heap:
            val h__.heappop(heap)
            prev.next ListNode(val)
            prev prev.next
        r.. dummy.next
    
    ___ test
        testCases [
            [
                ListNode(-1, ListNode(-1, ListNode(-1))),
                ListNode(-2, ListNode(-2, ListNode(-1))),
            ],
        ]
        ___ lists __ testCases:
            node mergeKLists(lists)
            w.... node:
                print('%s -> ' % node.val, e.._'')
                node node.next
            print('')
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
