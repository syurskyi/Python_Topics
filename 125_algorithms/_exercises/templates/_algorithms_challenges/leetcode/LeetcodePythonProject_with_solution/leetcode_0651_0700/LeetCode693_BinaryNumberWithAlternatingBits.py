'''
Created on Oct 25, 2017

@author: MT
'''
c_ Solution(o..
    ___ hasAlternatingBits  n
        """
        :type n: int
        :rtype: bool
        """
        prev n&1
        n >>= 1
        w.... n > 0:
            digit n & 1
            __ n.. digit ^ prev:
                r.. F..
            prev digit
            n >>= 1
        r.. T..
    
    ___ test
        testCases [
            4,
            5,
            7,
            11,
            10,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result hasAlternatingBits(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
