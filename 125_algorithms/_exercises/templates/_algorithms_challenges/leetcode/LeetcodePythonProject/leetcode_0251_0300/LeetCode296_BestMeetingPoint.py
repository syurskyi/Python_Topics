'''
Created on Mar 8, 2017

@author: MT
'''

class Solution(object
    ___ minTotalDistance(self, grid
        m, n = le.(grid), le.(grid[0])
        rows, cols = [], []
        ___ i in range(m
            ___ j in range(n
                __ grid[i][j] __ 1:
                    rows.append(i)
                    cols.append(j)
        cols.sort()
        sumVal = 0
        ___ row in rows:
            sumVal += abs(row - rows[le.(rows)//2])
        ___ col in cols:
            sumVal += abs(col - cols[le.(cols)//2])
        r_ sumVal
    
    ___ test(self
        testCases = [
            [
                '10001',
                '00000',
                '00100',
            ],
        ]
        ___ grid in testCases:
            grid = [[int(x) ___ x in l] ___ l in grid]
            print('grid: %s' % (grid))
            result = self.minTotalDistance(grid)
            print('result: %s' % (result))
            print('-='*20 + '-')

__ __name__ __ '__main__':
    Solution().test()
