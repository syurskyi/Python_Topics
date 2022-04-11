'''
Created on Feb 16, 2017

@author: MT
'''

c_ Solution(o..
    ___ numIslands  grid
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        __ n.. grid: r.. 0
        m, n l..(grid), l..(grid[0])
        res 0
        ___ i __ r..(m
            ___ j __ r..(n
                __ grid[i][j] __ '1':
                    grid[i][j] '#'
                    res += 1
                    bfs(grid, i, j)
        r.. res
    
    ___ bfs  grid, i, j
        queue [(i, j)]
        m, n l..(grid), l..(grid[0])
        w.... queue:
            i, j queue.p.. 0)
            ___ x, y __ (i+1, j), (i, j+1), (i-1, j), (i, j-1
                __ 0 <_ x < m a.. 0 <_ y < n a.. grid[x][y] __ '1':
                    grid[x][y] '#'
                    queue.a..([x, y])
    
    ___ test
        testCases [
#             [
#                 '11110',
#                 '11010',
#                 '11000',
#                 '00000',
#             ],
            [
                '11000',
                '11000',
                '00100',
                '00011',
            ],
        ]
        ___ grid __ testCases:
            grid [l..(x) ___ x __ grid]
            result numIslands(grid)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
