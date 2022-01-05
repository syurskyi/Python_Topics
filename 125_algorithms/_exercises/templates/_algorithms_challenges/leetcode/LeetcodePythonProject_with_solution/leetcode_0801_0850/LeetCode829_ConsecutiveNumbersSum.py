'''
Created on May 6, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ consecutiveNumbersSum  N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        res = 1
        i = 3
        w.... n%2 __ 0:
            n /= 2
        w.... i*i <= n:
            count = 0
            w.... n%i __ 0:
                n //= i
                count += 1
            res *= count+1
            i += 2
        r.. res __ n __ 1 ____ res*2
