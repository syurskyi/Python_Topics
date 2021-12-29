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
        m, n = len(matrix), len(matrix[0])
        for i in range(m-1, 0, -1):
            val = matrix[i][0]
            for k in range(1, n):
                __ i+k >= m or k >= n:
                    break
                __ matrix[i+k][k] != val:
                    return False
        for j in range(n):
            val = matrix[0][j]
            for k in range(1, m):
                __ j+k >= n or k >= m:
                    break
                __ matrix[k][j+k] != val:
                    return False
        return True
    
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
        for matrix in testCases:
            result = self.isToeplitzMatrix(matrix)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
