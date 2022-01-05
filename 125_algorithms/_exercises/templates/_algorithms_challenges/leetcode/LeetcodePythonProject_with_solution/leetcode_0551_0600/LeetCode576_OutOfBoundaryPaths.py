'''
Created on Sep 4, 2017

@author: MT
'''
c_ Solution(o..):
    ___ findPaths  m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        __ N < 0: r.. 0
        mod = 10**9+7
        count = [[0]*n ___ _ __ r..(m)]
        count[i][j] = 1
        result = 0
        ___ _ __ r..(N):
            tmp = [[0]*n ___ _ __ r..(m)]
            ___ r __ r..(m):
                ___ c __ r..(n):
                    ___ nr, nc __ (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                        __ 0 <= nr < m a.. 0 <= nc < n:
                            tmp[nr][nc] = (tmp[nr][nc]+count[r][c])%mod
                        ____:
                            result = (result+count[r][c])%mod
            count = tmp
        r.. result
    
    ___ test
        testCases = [
            [2, 2, 2, 0, 0],
            [1, 3, 3, 0, 1],
        ]
        ___ m, n, N, i, j __ testCases:
            print('m: %s' % m)
            print('n: %s' % n)
            print('N: %s' % N)
            print('i: %s' % i)
            print('j: %s' % j)
            result = findPaths(m, n, N, i, j)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
