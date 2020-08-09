'''
Created on Oct 16, 2019

@author: tongq
'''
class Solution(object
    ___ projectionArea(self, grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = le.(grid)
        res = 0
        ___ i in range(n
            maxNum = 0
            ___ j in range(n
                __ grid[i][j]:
                    res += 1
                maxNum = max(maxNum, grid[i][j])
            res += maxNum
        ___ j in range(n
            maxNum = 0
            ___ i in range(n
                maxNum = max(maxNum, grid[i][j])
            res += maxNum
        r_ res
    
    ___ test(self
        testCases = [
            [[2]],
            [[1,0],[0,2]],
            [[1,1,1],[1,0,1],[1,1,1]],
        ]
        ___ grid in testCases:
            res = self.projectionArea(grid)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
