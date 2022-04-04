'''
Created on Jan 22, 2017

@author: MT
'''

c_ Solution(o..
    ___ mySqrt  x
        """
        :type x: int
        :rtype: int
        """
        start, end = 1, x
        w.... start <_ end:
            mid = (start+end)/2
            __ mid*mid __ x:
                r.. mid
            ____ mid*mid < x:
                start = mid+1
            ____
                end = mid-1
        r.. start __ start __ 0 ____ start-1
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()