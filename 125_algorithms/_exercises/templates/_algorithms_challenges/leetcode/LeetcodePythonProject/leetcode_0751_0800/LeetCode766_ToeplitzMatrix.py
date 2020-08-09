'''
Created on Apr 3, 2018

@author: tongq
'''
class Solution(object
    ___ isToeplitzMatrix(self, matrix
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n = le.(matrix), le.(matrix[0])
        ___ i in range(m-1, 0, -1
            val = matrix[i][0]
            ___ k in range(1, n
                __ i+k >= m or k >= n:
                    break
                __ matrix[i+k][k] != val:
                    r_ False
        ___ j in range(n
            val = matrix[0][j]
            ___ k in range(1, m
                __ j+k >= n or k >= m:
                    break
                __ matrix[k][j+k] != val:
                    r_ False
        r_ True
    
    ___ test(self
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
        ___ matrix in testCases:
            result = self.isToeplitzMatrix(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
