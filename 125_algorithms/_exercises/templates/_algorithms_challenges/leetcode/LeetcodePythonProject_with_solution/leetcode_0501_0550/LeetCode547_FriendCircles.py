'''
Created on Aug 20, 2017

@author: MT
'''

class Solution(object):
    ___ findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        matrix = M
        n = len(matrix)
        roots = [-1]*n
        count = n
        for i in range(n):
            for j in range(n):
                __ i > j and matrix[i][j] == 1:
                    root1 = self.getRoot(roots, i)
                    root2 = self.getRoot(roots, j)
                    __ root1 != root2:
                        count -= 1
                        roots[root1] = root2
        return count
    
    ___ getRoot(self, roots, num):
        while roots[num] != -1:
            num = roots[num]
        return num
    
    ___ test(self):
        testCases = [
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1],
            ],
            [
                [1,1,0],
                [1,1,0],
                [0,0,1],
            ],
            [
                [1,1,0],
                [1,1,1],
                [0,1,1],
            ],
            [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]],
        ]
        for matrix in testCases:
            print('matrix:')
            print('\n'.join([str(row) for row in matrix]))
            res = self.findCircleNum(matrix)
            print('result: %s' % res)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
