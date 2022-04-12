'''
Created on May 10, 2017

@author: MT
'''

c_ Solution(o..
    ___ findMaximizedCapital  k, W, Profits, Capital
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        _______ h__
        heapCap    # list
        heapPro    # list
        ___ c, p __ z..(Capital, Profits
            h__.heappush(heapCap, (c, p
        ___ _ __ r..(k
            w.... heapCap a.. heapCap 0 0  <_ W:
                c, p h__.heappop(heapCap)
                h__.heappush(heapPro, (-p, c
            __ n.. heapPro:
                _____
            p, c h__.heappop(heapPro)
            W += -p
        r.. W
