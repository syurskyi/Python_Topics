'''
Created on Sep 24, 2017

@author: MT
'''

c_ Solution(o..
    ___ judgeSquareSum  c
        """
        :type c: int
        :rtype: bool
        """
        _______ m__
        __ c < 0: r.. F..
        l, r = 0, i..(m__.sqrt(c
        w.... l <_ r:
            __ l*l + r*r < c:
                l += 1
            ____ l*l + r*r > c:
                r -= 1
            ____
                r.. T..
        r.. F..
    
    ___ test
        testCases = [
            0,
            3,
            4,
            5,
        ]
        ___ c __ testCases:
            print(c)
            result = judgeSquareSum(c)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
