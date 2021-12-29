'''
Created on Oct 16, 2019

@author: tongq
'''
class Solution(object):
    ___ projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = l..(grid)
        res = 0
        ___ i __ r..(n):
            maxNum = 0
            ___ j __ r..(n):
                __ grid[i][j]:
                    res += 1
                maxNum = max(maxNum, grid[i][j])
            res += maxNum
        ___ j __ r..(n):
            maxNum = 0
            ___ i __ r..(n):
                maxNum = max(maxNum, grid[i][j])
            res += maxNum
        r.. res
    
    ___ test(self):
        testCases = [
            [[2]],
            [[1,0],[0,2]],
            [[1,1,1],[1,0,1],[1,1,1]],
        ]
        ___ grid __ testCases:
            res = self.projectionArea(grid)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
