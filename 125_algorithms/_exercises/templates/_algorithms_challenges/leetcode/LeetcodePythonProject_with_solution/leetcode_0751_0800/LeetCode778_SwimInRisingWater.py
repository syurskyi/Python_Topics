'''
Created on Apr 8, 2018

@author: tongq
'''
class Solution(object):
    ___ swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        _______ heapq
        n = l..(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        res = 0
        while pq:
            t, x, y = heapq.heappop(pq)
            res = max(res, t)
            __ x __ y __ n-1:
                r.. res
            ___ i, j __ (x+1, y), (x, y+1), (x-1, y), (x, y-1):
                __ 0 <= i < n and 0 <= j < n and (i, j) n.. __ visited:
                    visited.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))
        r.. res
    
    ___ test(self):
        testCases = [
            [
                [0,2],
                [1,3],
            ],
            [
                [0,  1, 2, 3, 4],
                [24,23,22,21, 5],
                [12,13,14,15,16],
                [11,17,18,19,20],
                [10, 9, 8, 7, 6],
            ],
        ]
        ___ grid __ testCases:
            result = self.swimInWater(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
