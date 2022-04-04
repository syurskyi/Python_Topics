'''
Created on Oct 8, 2017

@author: MT
'''
c_ Solution(o..
    ___ imageSmoother  M
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        _______ m__
        matrix = M
        __ n.. matrix o. n.. matrix[0]:
            r.. []
        m, n = l..(matrix), l..(matrix[0])
        res = [[0]*n ___ _ __ r..(m)]
        ___ i __ r..(m
            ___ j __ r..(n
                count = f__(matrix[i][j])
                num = 1.0
                ___ x, y __ (i+1, j), (i-1, j), (i, j+1), (i, j-1),\
                    (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1
                    __ 0 <_ x < m a.. 0 <_ y < n:
                        __ matrix[x][y] != 0:
                            count += f__(matrix[x][y])
                        num += 1
                tmp = i..(m__.f..(count/num
                res[i][j] = tmp
        r.. res
    
    ___ test
        testCases = [
            [
                [2,3],
            ],
            [
                [1,1,1],
                [1,0,1],
                [1,1,1],
            ],
            [
                [2, 3, 4],
                [5, 6, 7],
                [8, 9, 10],
                [11,12,13],
                [14,15,16],
            ]
        ]
        ___ matrix __ testCases:
            print('matrix:')
            print('\n'.j..([s..(row) ___ row __ matrix]
            result = imageSmoother(matrix)
            print('result:')
            print('\n'.j..([s..(row) ___ row __ result]
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
