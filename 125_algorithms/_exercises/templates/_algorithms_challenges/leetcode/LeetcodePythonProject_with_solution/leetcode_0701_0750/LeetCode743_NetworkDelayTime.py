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
        import heapq
        path = {}
        for time in times:
            sourceMap = path.get(time[0], {})
            __ time[1] not in sourceMap or sourceMap[time[1]] > time[2]:
                sourceMap[time[1]] = time[2]
            path[time[0]] = sourceMap
        
        distanceMap = {K:0}
        heap = []
        heapq.heappush(heap, [0, K])
        maxVal = -1
        while heap:
            d, node = heapq.heappop(heap)
            __ node in distanceMap and distanceMap[node] < d:
                continue
            __ node in path:
                for node0 in path[node]:
                    absDist = d+path[node][node0]
                    __ node0 in distanceMap and distanceMap[node0] <= absDist:
                        continue
                    distanceMap[node0] = absDist
                    heapq.heappush(heap, [absDist, node0])
        for val in distanceMap.values():
            __ val > maxVal:
                maxVal = val
        return maxVal __ len(distanceMap) == N else -1
    
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
        for times, N, K in testCases:
            result = self.networkDelayTime(times, N, K)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
