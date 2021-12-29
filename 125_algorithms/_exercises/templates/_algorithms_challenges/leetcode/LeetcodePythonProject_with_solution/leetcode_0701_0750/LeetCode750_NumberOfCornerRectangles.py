'''
Created on Mar 25, 2018

@author: tongq
'''
class Solution(object):
    ___ countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m-1):
            for j in range(i+1, m):
                counter = 0
                for k in range(n):
                    __ grid[i][k] == 1 and grid[j][k] == 1:
                        counter += 1
                __ counter > 0:
                    res += counter*(counter-1)//2
        return res
    
    ___ test(self):
        testCases = [
            [
                [1, 0, 0, 1, 0],
                [0, 0, 1, 0, 1],
                [0, 0, 0, 1, 0],
                [1, 0, 1, 0, 1]
            ],
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
            [
                [1, 1, 1, 1],
            ],
        ]
        for grid in testCases:
            result = self.countCornerRectangles(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
