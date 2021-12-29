'''
Created on Oct 31, 2019

@author: tongq
'''
class Solution(object):
    ___ surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = l..(grid), l..(grid[0])
        res = 0
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ (grid[i][j]):
                    res += 2+grid[i][j]*4
                __ i > 0:
                    res -= m..(grid[i-1][j], grid[i][j])*2
                __ j > 0:
                    res -= m..(grid[i][j-1], grid[i][j])*2
        r.. res
    
    ___ test(self):
        testCases = [
            [[1,0],[0,2]],
            [[1,1,1],[1,0,1],[1,1,1]],
            [[2,2,2],[2,1,2],[2,2,2]],
        ]
        ___ grid __ testCases:
            res = self.surfaceArea(grid)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
