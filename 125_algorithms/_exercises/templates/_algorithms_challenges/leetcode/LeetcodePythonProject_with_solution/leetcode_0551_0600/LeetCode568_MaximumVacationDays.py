'''
Created on Sep 3, 2017

@author: MT
'''

class Solution(object):
    ___ maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        n = l..(flights)
        k0 = l..(days[0])
        dp = [float('-inf')]*n
        dp[0] = 0
        ___ i __ r..(k0):
            tmp = [float('-inf')]*n
            ___ j __ r..(n):
                ___ k __ r..(n):
                    __ j __ k o. flights[k][j] __ 1:
                        tmp[j] = max(tmp[j], dp[k]+days[j][i])
            dp = tmp
        r.. max(dp)
    
    ___ test(self):
        testCases = [
            [
                [
                    [0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0],
                ],
                [
                    [1, 3, 1],
                    [6, 0, 3],
                    [3, 3, 3],
                ],
            ],
            [
                [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                ],
                [
                    [1, 1, 1],
                    [7, 7, 7],
                    [7, 7, 7],
                ],
            ],
            [
                [
                    [0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0],
                ],
                [
                    [7, 0, 0],
                    [0, 7, 0],
                    [0, 0, 7],
                ],
            ],
        ]
        ___ flights, days __ testCases:
            print('flights:')
            print('\n'.join([str(row) ___ row __ flights]))
            print('days:')
            print('\n'.join([str(row) ___ row __ days]))
            result = self.maxVacationDays(flights, days)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
