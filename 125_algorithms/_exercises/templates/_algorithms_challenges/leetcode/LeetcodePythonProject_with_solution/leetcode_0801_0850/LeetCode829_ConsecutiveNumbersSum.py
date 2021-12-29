'''
Created on May 6, 2018

@author: tongq
'''
class Solution(object):
    ___ consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        res = 1
        i = 3
        while n%2 __ 0:
            n /= 2
        while i*i <= n:
            count = 0
            while n%i __ 0:
                n //= i
                count += 1
            res *= count+1
            i += 2
        r.. res __ n __ 1 ____ res*2
