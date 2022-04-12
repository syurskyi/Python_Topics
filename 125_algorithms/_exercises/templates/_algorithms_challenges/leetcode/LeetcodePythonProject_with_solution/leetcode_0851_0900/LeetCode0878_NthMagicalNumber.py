'''
Created on Oct 13, 2019

@author: tongq
'''
c_ Solution(o..
    ___ nthMagicalNumber  N, A, B
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        n, a, b N, A, B
        w.... b:
            a, b b, a_b
        l, r, lcm 2, 10**14, A*B // a
        w.... l < r:
            m (l+r)//2
            __ m // A + m // B - m // lcm < n:
                l m+1
            ____
                r m
        r.. l % (10**9+7)
    
    ___ test
        testCases [
            [5, 2, 4],
        ]
        ___ n, a, b __ testCases:
            res nthMagicalNumber(n, a, b)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
