'''
Created on Apr 24, 2018

@author: tongq
'''
c_ Solution(o..
    ___ maxIncreaseKeepingSkyline  grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n l..(grid), l..(grid 0
        rows [[0, 0] ___ _ __ r..(m)]
        cols [[0, 0] ___ _ __ r..(n)]
        sumVal 0
        ___ i __ r..(m
            ___ j __ r..(n
                sumVal += grid[i][j]
                __ grid[i][j] > rows[i][0]:
                    rows[i][1] j
                    rows[i][0] grid[i][j]
                __ grid[i][j] > cols[j][0]:
                    cols[j][1] i
                    cols[j][0] grid[i][j]
        res 0
        ___ i __ r..(m
            ___ j __ r..(n
                res += m..(rows[i][0], cols[j] 0
        r.. res - sumVal
    
    ___ test
        testCases [
            [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]],
        ]
        ___ grid __ testCases:
            result maxIncreaseKeepingSkyline(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
