'''
Created on Mar 25, 2018

@author: tongq
'''
class Solution(object
    ___ countCornerRectangles(self, grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        m, n = le.(grid), le.(grid[0])
        ___ i in range(m-1
            ___ j in range(i+1, m
                counter = 0
                ___ k in range(n
                    __ grid[i][k] __ 1 and grid[j][k] __ 1:
                        counter += 1
                __ counter > 0:
                    res += counter*(counter-1)//2
        r_ res
    
    ___ test(self
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
        ___ grid in testCases:
            result = self.countCornerRectangles(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
