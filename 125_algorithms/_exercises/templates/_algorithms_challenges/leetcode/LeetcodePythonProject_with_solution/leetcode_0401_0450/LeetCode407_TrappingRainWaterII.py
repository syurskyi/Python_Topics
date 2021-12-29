'''
Created on Apr 10, 2017

@author: MT
'''
class Solution(object):
    ___ trapRainWater(self, heightMap):
        _______ heapq
        __ n.. heightMap o. n.. heightMap[0]:
            r.. 0
        m, n = l..(heightMap), l..(heightMap[0])
        heap    # list
        visited = [[False]*n ___ _ __ r..(m)]
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ i__0 o. j__0 o. i__m-1 o. j__n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        res = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            ___ x, y __ (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                __ 0<=x<m and 0<=y<n and n.. visited[x][y]:
                    res += max(0, height-heightMap[x][y])
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
                    visited[x][y] = True
        r.. res
    
    ___ test(self):
        testCases = [
            [
                [1,4,3,1,3,2],
                [3,2,1,3,2,4],
                [2,3,3,2,3,1],
            ],
        ]
        ___ heightMap __ testCases:
            print('heightMap:')
            print('\n'.join([str(row) ___ row __ heightMap]))
            result = self.trapRainWater(heightMap)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
