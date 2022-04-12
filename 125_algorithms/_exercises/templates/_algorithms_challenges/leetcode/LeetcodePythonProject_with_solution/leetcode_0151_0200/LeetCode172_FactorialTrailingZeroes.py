'''
Created on Feb 13, 2017

@author: MT
'''

c_ Solution(o..
    ___ trailingZeroes  n
        """
        :type n: int
        :rtype: int
        """
        __ n < 0: r.. -1
        count 0
        i 5
        w.... n//i > 0
            count += n//i
            i *= 5
        r.. count
    
    ___ test
        testCases [
            3,
            5,
            10,
        ]
        ___ n __ testCases:
            print('n: %s' % (n
            result trailingZeroes(n)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()