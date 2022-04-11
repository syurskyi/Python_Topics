'''
Created on Mar 11, 2017

@author: MT
'''
c_ Solution(o..
    ___ numIslands2  m, n, positions
        res    # list
        roots [-1]*(m*n)
        grid [[F..]*n ___ _ __ r..(m)]
        count 0
        ___ pos __ positions:
            i, j pos[0], pos[1]
            grid[i][j] T..
            count += 1
            root0 i*n+j
            ___ x, y __ (i+1, j), (i-1, j), (i, j+1), (i, j-1
                __ 0 <_ x < m a.. 0 <_ y < n a.. grid[x][y]:
                    root getRoot(roots, x*n+y)
                    __ root != root0:
                        count -_ 1
                        roots[root] root0
            res.a..(count)
        r.. res
    
    ___ getRoot  roots, ind
        w.... roots[ind] != -1:
            ind roots[ind]
        r.. ind
    
    ___ test
        testCases [
            (3, 3, [[0,0], [0,1], [1,2], [2,1]]),
            [
                3,
                3,
                [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]],
            ],
            [
                8,
                4,
                [[0,0],[7,1],[6,1],[3,3],[4,1]],
            ],
        ]
        ___ m, n, positions __ testCases:
            print('m: %s' % (m
            print('n: %s' % (n
            print('positions: %s' % (positions
            result numIslands2(m, n, positions)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
