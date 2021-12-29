'''
Created on Mar 21, 2018

@author: tongq
'''
class Solution(object):
    ___ networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        _______ heapq
        path = {}
        ___ time __ times:
            sourceMap = path.get(time[0], {})
            __ time[1] n.. __ sourceMap o. sourceMap[time[1]] > time[2]:
                sourceMap[time[1]] = time[2]
            path[time[0]] = sourceMap
        
        distanceMap = {K:0}
        heap    # list
        heapq.heappush(heap, [0, K])
        maxVal = -1
        while heap:
            d, node = heapq.heappop(heap)
            __ node __ distanceMap and distanceMap[node] < d:
                continue
            __ node __ path:
                ___ node0 __ path[node]:
                    absDist = d+path[node][node0]
                    __ node0 __ distanceMap and distanceMap[node0] <= absDist:
                        continue
                    distanceMap[node0] = absDist
                    heapq.heappush(heap, [absDist, node0])
        ___ val __ distanceMap.values():
            __ val > maxVal:
                maxVal = val
        r.. maxVal __ l..(distanceMap) __ N ____ -1
    
    ___ test(self):
        testCases = [
            [
                [[2,1,1],[2,3,1],[3,4,1]],
                4,
                2,
            ],
            [
                [[1,2,1],[2,3,2],[1,3,4]],
                3,
                1,
            ],
        ]
        ___ times, N, K __ testCases:
            result = self.networkDelayTime(times, N, K)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
