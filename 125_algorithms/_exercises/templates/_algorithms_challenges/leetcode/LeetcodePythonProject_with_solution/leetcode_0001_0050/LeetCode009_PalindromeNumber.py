'''
Created on Jan 7, 2017

@author: MT
'''
c_ Solution(o..
    ___ isPalindrome  x
        """
        :type x: int
        :rtype: bool
        """
        __ x < 0: r.. F..
        div = 1
        w.... x//div >= 10:
            div *= 10
        w.... x > 0:
            first = x//div
            last  = x%10
            __ first != last:
                r.. F..
            x -= first*div
            x = (x-last)//10
            div //= 100
        r.. T..
    
    ___ test
        testCases = [
            123,
            121,
            1,
            223322,
            2442,
            24423,
            2453,
            100021,
        ]
        ___ x __ testCases:
            print('x: %s' % (x
            result = isPalindrome(x)
            print('result: %s' % (result
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
