'''
Created on Oct 3, 2019

@author: tongq
'''
class Solution(object
    ___ minRefuelStops(self, target, startFuel, stations
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        ______ heapq
        h = []
        res = i = 0
        cur = startFuel
        w___ cur < target:
            w___ i < le.(stations) and stations[i][0] <= cur:
                heapq.heappush(h, -stations[i][1])
                i += 1
            __ not h:
                r_ -1
            cur += -heapq.heappop(h)
            res += 1
        r_ res
