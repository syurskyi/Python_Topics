'''
Created on Sep 17, 2019

@author: tongq
'''
c_ Solution(o..
    ___ matrixScore  A
        """
        :type A: List[List[int]]
        :rtype: int
        """
        matrix A
        __ n.. matrix: r.. 0
        m, n l..(matrix), l..(matrix[0])
        ___ i __ r..(m
            __ matrix[i][0] __ 0:
                ___ j __ r..(n
                    matrix[i][j] 0 __ matrix[i][j] ____ 1
        ___ j __ r..(1, n
            count 0
            ___ i __ r..(m
                __ matrix[i][j] __ 1:
                    count += 1
            __ 2*count < m:
                ___ i __ r..(m
                    matrix[i][j] 0 __ matrix[i][j] ____ 1
        res 0
        ___ i __ r..(m
            num 0
            ___ j __ r..(n
                num num*2 + matrix[i][j]
            res += num
        r.. res
    
    ___ test
        testCase [
#             [
#                 [0,0,1,1],
#                 [1,0,1,0],
#                 [1,1,0,0]
#             ],
            [
                [0,1],
                [1,1]
            ],
        ]
        ___ matrix __ testCase:
            res matrixScore(matrix)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()

