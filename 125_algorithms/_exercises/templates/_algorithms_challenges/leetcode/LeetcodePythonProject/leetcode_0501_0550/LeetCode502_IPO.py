'''
Created on May 10, 2017

@author: MT
'''

class Solution(object
    ___ findMaximizedCapital(self, k, W, Profits, Capital
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        ______ heapq
        heapCap = []
        heapPro = []
        ___ c, p in zip(Capital, Profits
            heapq.heappush(heapCap, (c, p))
        ___ _ in range(k
            w___ heapCap and heapCap[0][0] <= W:
                c, p = heapq.heappop(heapCap)
                heapq.heappush(heapPro, (-p, c))
            __ not heapPro:
                break
            p, c = heapq.heappop(heapPro)
            W += -p
        r_ W
