'''
Created on Apr 15, 2018

@author: tongq
'''
c_ Solution(o..
    ___ numTilings  N
        """
        :type N: int
        :rtype: int
        """
        mod 10**9+7
        p3 -1
        p2 0
        p1 1
        ___ _ __ r..(N
            cur (p1*2+p3)%mod
            p3 p2
            p2 p1
            p1 cur
        r.. p1
    
    ___ test
        testCases [
            3,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result numTilings(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
