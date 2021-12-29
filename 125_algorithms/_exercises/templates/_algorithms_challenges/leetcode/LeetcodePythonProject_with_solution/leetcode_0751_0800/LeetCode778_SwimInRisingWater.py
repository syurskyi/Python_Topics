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
        import heapq
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        res = 0
        while pq:
            t, x, y = heapq.heappop(pq)
            res = max(res, t)
            __ x == y == n-1:
                return res
            for i, j in (x+1, y), (x, y+1), (x-1, y), (x, y-1):
                __ 0 <= i < n and 0 <= j < n and (i, j) not in visited:
                    visited.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))
        return res
    
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
        for grid in testCases:
            result = self.swimInWater(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
