'''
Created on Jan 21, 2017

@author: MT
'''

c_ Solution(o..
    ___ myPow  x, n
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        __ n __ 0:
            r.. 1
        __ n < 0:
            n -n
            x 1/x
        __ n%2__0:
            r.. myPow(x*x, n/2)
        ____
            r.. x*myPow(x*x, n/2)
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()