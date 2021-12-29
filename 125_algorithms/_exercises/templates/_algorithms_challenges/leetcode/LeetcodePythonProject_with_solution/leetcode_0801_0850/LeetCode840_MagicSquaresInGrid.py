'''
Created on Dec 20, 2018

@author: tongq
'''
class Solution(object):
    ___ numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = l..(grid), l..(grid[0])
        res = 0
        ___ i __ r..(m-2):
            ___ j __ r..(n-2):
                __ self.isValid(grid, i, j):
                    res += 1
        r.. res
    
    ___ isValid(self, grid, i, j):
        hashset = set([grid[i][j], grid[i][j+1], grid[i][j+2],\
                       grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],\
                       grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]])
        __ hashset != set(r..(1, 10)):
            r.. False
        val = grid[i][j] + grid[i+1][j] + grid[i+2][j]
        __ val != grid[i][j] + grid[i][j+1] + grid[i][j+2] o.\
            val != grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] o.\
            val != grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] o.\
            val != grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] o.\
            val != grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] o.\
            val != grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] o.\
            val != grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]:
            r.. False
        r.. True
    
    ___ test(self):
        testCases = [
            [[4,3,8,4],[9,5,1,9],[2,7,6,2]],
        ]
        ___ grid __ testCases:
            result = self.numMagicSquaresInside(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
