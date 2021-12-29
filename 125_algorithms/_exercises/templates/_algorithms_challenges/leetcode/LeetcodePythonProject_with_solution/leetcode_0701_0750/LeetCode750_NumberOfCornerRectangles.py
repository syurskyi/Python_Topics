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
        m, n = l..(grid), l..(grid[0])
        ___ i __ r..(m-1):
            ___ j __ r..(i+1, m):
                counter = 0
                ___ k __ r..(n):
                    __ grid[i][k] __ 1 a.. grid[j][k] __ 1:
                        counter += 1
                __ counter > 0:
                    res += counter*(counter-1)//2
        r.. res
    
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
        ___ grid __ testCases:
            result = self.countCornerRectangles(grid)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
