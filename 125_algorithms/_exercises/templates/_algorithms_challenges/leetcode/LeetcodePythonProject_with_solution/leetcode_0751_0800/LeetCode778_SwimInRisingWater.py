'''
Created on Apr 8, 2018

@author: tongq
'''
c_ Solution(o..
    ___ swimInWater  grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        _______ heapq
        n l..(grid)
        pq [(grid 0 0 , 0, 0)]
        visited s..([(0, 0)])
        res 0
        w.... pq:
            t, x, y heapq.heappop(pq)
            res m..(res, t)
            __ x __ y __ n-1:
                r.. res
            ___ i, j __ (x+1, y), (x, y+1), (x-1, y), (x, y-1
                __ 0 <_ i < n a.. 0 <_ j < n a.. (i, j) n.. __ visited:
                    visited.add((i, j
                    heapq.heappush(pq, (grid[i][j], i, j
        r.. res
    
    ___ test
        testCases [
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
            result swimInWater(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
