'''
Created on Mar 16, 2017

@author: MT
'''

c_ Solution(o..):
    ___ shortestDistance  grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        __ n.. grid o. n.. grid[0]:
            r.. 0
        m, n = l..(grid), l..(grid[0])
        distance = [[0]*n ___ _ __ r..(m)]
        reach = [[0]*n ___ _ __ r..(m)]
        buildingNum = 0
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] __ 1:
                    buildingNum += 1
                    queue = [(i, j)]
                    visited = [[F..]*n ___ _ __ r..(m)]
                    level = 1
                    w.... queue:
                        size = l..(queue)
                        ___ _ __ r..(size):
                            i0, j0 = queue.pop(0)
                            ___ x, y __ (i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1):
                                __ 0 <= x < m a.. 0 <= y < n a..\
                                    n.. visited[x][y] a.. grid[x][y] __ 0:
                                    distance[x][y] += level
                                    reach[x][y] += 1
                                    visited[x][y] = T..
                                    queue.a..((x, y))
                        level += 1
        res = f__('inf')
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] __ 0 a.. reach[i][j] __ buildingNum:
                    res = m..(res, distance[i][j])
        r.. res __ res != f__('inf') ____ -1
    
    ___ test
        testCases = [
            [
                [1, 0, 2, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
            ]
        ]
        ___ grid __ testCases:
            result = shortestDistance(grid)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
