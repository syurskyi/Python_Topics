'''
Created on Oct 8, 2017

@author: MT
'''
class Solution(object
    ___ imageSmoother(self, M
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        ______ ma__
        matrix = M
        __ not matrix or not matrix[0]:
            r_ []
        m, n = le.(matrix), le.(matrix[0])
        res = [[0]*n ___ _ in range(m)]
        ___ i in range(m
            ___ j in range(n
                count = float(matrix[i][j])
                num = 1.0
                ___ x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1),\
                    (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1
                    __ 0 <= x < m and 0 <= y < n:
                        __ matrix[x][y] != 0:
                            count += float(matrix[x][y])
                        num += 1
                tmp = int(ma__.fl..(count/num))
                res[i][j] = tmp
        r_ res
    
    ___ test(self
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
        ___ matrix in testCases:
            print('matrix:')
            print('\n'.join([str(row) ___ row in matrix]))
            result = self.imageSmoother(matrix)
            print('result:')
            print('\n'.join([str(row) ___ row in result]))
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
