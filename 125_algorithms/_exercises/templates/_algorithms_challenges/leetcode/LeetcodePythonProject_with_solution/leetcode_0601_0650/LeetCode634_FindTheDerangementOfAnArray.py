'''
Created on Sep 24, 2017

@author: MT
'''
c_ Solution(o..
    ___ findDerangement  n
        """
        :type n: int
        :rtype: int
        """
        dn1, dn2 = 1, 0
        __ n <_ 1: r.. 0
        res = 1
        ___ i __ r..(3, n+1
            res = ((i-1)*(dn1+dn2%(10**9+7)
            dn2 = dn1
            dn1 = res
        r.. i..(res)
    
    ___ test
        testCases = [
            1,
            2,
            3,
            4,
            10,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = findDerangement(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
