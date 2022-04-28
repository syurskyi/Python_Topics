'''
Created on Sep 3, 2017

@author: MT
'''

c_ Solution(o..
    ___ maxVacationDays  flights, days
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        n l..(flights)
        k0 l..(days 0
        dp [f__ '-inf']*n
        dp[0] 0
        ___ i __ r..(k0
            tmp  [f__ '-inf']*n
            ___ j __ r..(n
                ___ k __ r..(n
                    __ j __ k o. flights[k][j] __ 1:
                        tmp[j] m..(tmp[j], dp[k]+days[j][i])
            dp tmp
        r.. m..(dp)
    
    ___ test
        testCases [
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
            print('\n'.j..([s..(row) ___ row __ flights]
            print('days:')
            print('\n'.j..([s..(row) ___ row __ days]
            result maxVacationDays(flights, days)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
