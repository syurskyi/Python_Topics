'''
Created on Nov 6, 2017

@author: MT
'''
# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, val, nextNode=None
        self.val = val
        self.next = nextNode

class Solution(object
    ___ mergeKLists(self, lists
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ______ heapq
        heap = []
        ___ l in lists:
            w___ l:
                heapq.heappush(heap, l.val)
                l = l.next
        dummy = ListNode(-1)
        prev = dummy
        w___ heap:
            val = heapq.heappop(heap)
            prev.next = ListNode(val)
            prev = prev.next
        r_ dummy.next
    
    ___ test(self
        testCases = [
            [
                ListNode(-1, ListNode(-1, ListNode(-1))),
                ListNode(-2, ListNode(-2, ListNode(-1))),
            ],
        ]
        ___ lists in testCases:
            node = self.mergeKLists(lists)
            w___ node:
                print('%s -> ' % node.val, end='')
                node = node.next
            print('')
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
