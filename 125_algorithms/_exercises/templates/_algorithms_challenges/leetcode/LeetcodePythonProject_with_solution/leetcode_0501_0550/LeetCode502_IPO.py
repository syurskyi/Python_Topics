'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    ___ findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        _______ heapq
        heapCap    # list
        heapPro    # list
        ___ c, p __ zip(Capital, Profits):
            heapq.heappush(heapCap, (c, p))
        ___ _ __ r..(k):
            while heapCap and heapCap[0][0] <= W:
                c, p = heapq.heappop(heapCap)
                heapq.heappush(heapPro, (-p, c))
            __ n.. heapPro:
                break
            p, c = heapq.heappop(heapPro)
            W += -p
        r.. W
