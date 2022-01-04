'''
Created on Apr 3, 2018

@author: tongq
'''
c_ Solution(object):
    ___ isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n = l..(matrix), l..(matrix[0])
        ___ i __ r..(m-1, 0, -1):
            val = matrix[i][0]
            ___ k __ r..(1, n):
                __ i+k >= m o. k >= n:
                    break
                __ matrix[i+k][k] != val:
                    r.. F..
        ___ j __ r..(n):
            val = matrix[0][j]
            ___ k __ r..(1, m):
                __ j+k >= n o. k >= m:
                    break
                __ matrix[k][j+k] != val:
                    r.. F..
        r.. T..
    
    ___ test
        testCases = [
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
            result = isToeplitzMatrix(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
