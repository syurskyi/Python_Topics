'''
Created on Mar 8, 2017

@author: MT
'''

c_ Solution(object):
    ___ minTotalDistance(self, grid):
        m, n = l..(grid), l..(grid[0])
        rows, cols    # list, []
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ grid[i][j] __ 1:
                    rows.a..(i)
                    cols.a..(j)
        cols.s..()
        sumVal = 0
        ___ row __ rows:
            sumVal += abs(row - rows[l..(rows)//2])
        ___ col __ cols:
            sumVal += abs(col - cols[l..(cols)//2])
        r.. sumVal
    
    ___ test
        testCases = [
            [
                '10001',
                '00000',
                '00100',
            ],
        ]
        ___ grid __ testCases:
            grid = [[i..(x) ___ x __ l] ___ l __ grid]
            print('grid: %s' % (grid))
            result = minTotalDistance(grid)
            print('result: %s' % (result))
            print('-='*20 + '-')

__ _____ __ _____
    Solution().test()
