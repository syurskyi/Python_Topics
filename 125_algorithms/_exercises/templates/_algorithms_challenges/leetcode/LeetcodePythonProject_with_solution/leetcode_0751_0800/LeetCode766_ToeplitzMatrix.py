'''
Created on Apr 3, 2018

@author: tongq
'''
class Solution(object):
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
                    r.. False
        ___ j __ r..(n):
            val = matrix[0][j]
            ___ k __ r..(1, m):
                __ j+k >= n o. k >= m:
                    break
                __ matrix[k][j+k] != val:
                    r.. False
        r.. True
    
    ___ test(self):
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
            result = self.isToeplitzMatrix(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
