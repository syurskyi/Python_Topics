'''
Created on Aug 20, 2017

@author: MT
'''

c_ Solution(object):
    ___ findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        matrix = M
        n = l..(matrix)
        roots = [-1]*n
        count = n
        ___ i __ r..(n):
            ___ j __ r..(n):
                __ i > j a.. matrix[i][j] __ 1:
                    root1 = getRoot(roots, i)
                    root2 = getRoot(roots, j)
                    __ root1 != root2:
                        count -= 1
                        roots[root1] = root2
        r.. count
    
    ___ getRoot(self, roots, num):
        w.... roots[num] != -1:
            num = roots[num]
        r.. num
    
    ___ test
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
        ___ matrix __ testCases:
            print('matrix:')
            print('\n'.j..([s..(row) ___ row __ matrix]))
            res = findCircleNum(matrix)
            print('result: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
