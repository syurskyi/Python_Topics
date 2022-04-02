'''
Created on Sep 30, 2019

@author: tongq
'''
c_ Solution(o..
    ___ binaryGap  N
        """
        :type N: int
        :rtype: int
        """
        n = N
        i = 0
        prev = -1
        res = 0
        w.... n > 0:
            d = n % 2
            __ d __ 1:
                __ prev >= 0:
                    res = m..(res, i-prev)
                prev = i
            n //= 2
            i += 1
        r.. res
