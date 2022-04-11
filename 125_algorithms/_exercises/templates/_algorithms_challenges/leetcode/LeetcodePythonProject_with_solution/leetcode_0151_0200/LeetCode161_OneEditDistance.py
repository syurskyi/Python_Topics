'''
Created on Feb 12, 2017

@author: MT
'''

c_ Solution(o..
    ___ isOneEditDistance  s, t
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ s __ N.. o. t __ N..
            r.. F..
        m, n l..(t), l..(s)
        __ a..(m-n) > 1:
            r.. F..
        i, j, count 0, 0, 0
        w.... i < n a.. j < m:
            __ s[i] __ t[j]:
                i+=1
                j+=1
            ____
                count+=1
                __ count>1:
                    r.. F..
                __ m>n:
                    j+=1
                ____ n>m:
                    i+=1
                ____
                    i+=1
                    j+=1
        __ i < n o. j < m:
            count += 1
        __ count __ 1:
            r.. T..
        r.. F..
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()
