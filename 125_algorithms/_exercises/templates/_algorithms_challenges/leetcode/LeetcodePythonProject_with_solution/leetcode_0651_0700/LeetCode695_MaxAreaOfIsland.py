'''
Created on Oct 25, 2017

@author: MT
'''
c_ Solution(o..
    ___ maxAreaOfIsland  grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        __ n.. grid o. n.. grid[0]:
            r.. 0
        m, n l..(grid), l..(grid 0
        maxArea 0
        ___ i __ r..(m
            ___ j __ r..(n
                maxArea m..(maxArea, bfs(grid, m, n, i, j
        r.. maxArea
    
    ___ bfs  grid, m, n, i, j
        __ grid[i][j] __ 0:
            r.. 0
        area 0
        grid[i][j] -1
        queue [(i, j)]
        w.... queue:
            i, j queue.p.. 0)
            area += 1
            ___ x, y __ (i+1, j), (i-1, j), (i, j+1), (i, j-1
                __ 0 <_ x < m a.. 0 <_ y < n a.. grid[x][y] __ 1:
                    queue.a..((x, y
                    grid[x][y] -1
        r.. area
    
    ___ test
        testCases [
            [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]],
        ]
        ___ grid __ testCases:
            result maxAreaOfIsland(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
