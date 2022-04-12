'''
Created on Apr 3, 2018

@author: tongq
'''
c_ Solution(o..
    ___ isToeplitzMatrix  matrix
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n l..(matrix), l..(matrix[0])
        ___ i __ r..(m-1, 0, -1
            val matrix[i][0]
            ___ k __ r..(1, n
                __ i+k >_ m o. k >_ n:
                    _____
                __ matrix[i+k][k] !_ val:
                    r.. F..
        ___ j __ r..(n
            val matrix[0][j]
            ___ k __ r..(1, m
                __ j+k >_ n o. k >_ m:
                    _____
                __ matrix[k][j+k] !_ val:
                    r.. F..
        r.. T..
    
    ___ test
        testCases [
            [
                [1,2,3,4],
                [5,1,2,3],
                [9,5,1,2]
            ],
            [
                [1,2],
                [2,2]
            ],
        ]
        ___ matrix __ testCases:
            result isToeplitzMatrix(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
