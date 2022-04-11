'''
Created on Oct 16, 2019

@author: tongq
'''
c_ Solution(o..
    ___ projectionArea  grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n l..(grid)
        res 0
        ___ i __ r..(n
            maxNum 0
            ___ j __ r..(n
                __ grid[i][j]:
                    res += 1
                maxNum m..(maxNum, grid[i][j])
            res += maxNum
        ___ j __ r..(n
            maxNum 0
            ___ i __ r..(n
                maxNum m..(maxNum, grid[i][j])
            res += maxNum
        r.. res
    
    ___ test
        testCases [
            [[2]],
            [[1,0],[0,2]],
            [[1,1,1],[1,0,1],[1,1,1]],
        ]
        ___ grid __ testCases:
            res projectionArea(grid)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
