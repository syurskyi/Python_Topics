'''
Created on Apr 10, 2017

@author: MT
'''
class Solution(object
    ___ trapRainWater(self, heightMap
        ______ heapq
        __ not heightMap or not heightMap[0]:
            r_ 0
        m, n = le.(heightMap), le.(heightMap[0])
        heap = []
        visited = [[False]*n ___ _ in range(m)]
        ___ i in range(m
            ___ j in range(n
                __ i__0 or j__0 or i__m-1 or j__n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        res = 0
        w___ heap:
            height, i, j = heapq.heappop(heap)
            ___ x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1
                __ 0<=x<m and 0<=y<n and not visited[x][y]:
                    res += max(0, height-heightMap[x][y])
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
                    visited[x][y] = True
        r_ res
    
    ___ test(self
        testCases = [
            [
                [1,4,3,1,3,2],
                [3,2,1,3,2,4],
                [2,3,3,2,3,1],
            ],
        ]
        ___ heightMap in testCases:
            print('heightMap:')
            print('\n'.join([str(row) ___ row in heightMap]))
            result = self.trapRainWater(heightMap)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
