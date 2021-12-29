'''
Created on Sep 17, 2019

@author: tongq
'''
class Solution(object):
    ___ matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        matrix = A
        __ not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            __ matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0 __ matrix[i][j] else 1
        for j in range(1, n):
            count = 0
            for i in range(m):
                __ matrix[i][j] == 1:
                    count += 1
            __ 2*count < m:
                for i in range(m):
                    matrix[i][j] = 0 __ matrix[i][j] else 1
        res = 0
        for i in range(m):
            num = 0
            for j in range(n):
                num = num*2 + matrix[i][j]
            res += num
        return res
    
    ___ test(self):
        testCase = [
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
        for matrix in testCase:
            res = self.matrixScore(matrix)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()

