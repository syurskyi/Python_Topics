'''
Created on Oct 3, 2019

@author: tongq
'''
c_ Solution(o..
    ___ minRefuelStops  target, startFuel, stations
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        _______ h__
        h    # list
        res i 0
        cur startFuel
        w.... cur < target:
            w.... i < l..(stations) a.. stations[i][0] <_ cur:
                h__.heappush(h, -stations[i][1])
                i += 1
            __ n.. h:
                r.. -1
            cur += -h__.heappop(h)
            res += 1
        r.. res
