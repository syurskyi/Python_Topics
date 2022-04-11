'''
Created on Apr 18, 2018

@author: tongq
'''
c_ Solution(o..
    ___ champagneTower  poured, query_row, query_glass
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        result [[0.0]*101 ___ _ __ r..(101)]
        result[0][0] poured
        ___ i __ r..(100
            ___ j __ r..(i+1
                __ result[i][j] >_ 1:
                    result[i+1][j] += (result[i][j]-1)/2.0
                    result[i+1][j+1] += (result[i][j]-1)/2.0
                    result[i][j] 1.0
        r.. result[query_row][query_glass]
    
    ___ test
        testCases [
            [1, 1, 1], # 0.0
            [2, 1, 1], # 0.5
            [2, 1, 0], # 0.5
            [6, 2, 0],
            [6, 2, 1],
            [6, 3, 1],
            [6, 3, 0]
        ]
        ___ poured, query_row, query_glass __ testCases:
            print('poured: %s' % poured)
            print('query_row: %s' % query_row)
            print('query_glass: %s' % query_glass)
            result champagneTower(poured, query_row, query_glass)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
