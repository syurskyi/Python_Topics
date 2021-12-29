'''
Created on Feb 12, 2017

@author: MT
'''

class Solution(object):
    ___ isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ s __ N.. o. t __ N..
            r.. False
        m, n = l..(t), l..(s)
        __ abs(m-n) > 1:
            r.. False
        i, j, count = 0, 0, 0
        while i < n and j < m:
            __ s[i] __ t[j]:
                i+=1
                j+=1
            ____:
                count+=1
                __ count>1:
                    r.. False
                __ m>n:
                    j+=1
                ____ n>m:
                    i+=1
                ____:
                    i+=1
                    j+=1
        __ i < n o. j < m:
            count += 1
        __ count __ 1:
            r.. True
        r.. False
    
    ___ test(self):
        pass

__ __name__ __ '__main__':
    Solution().test()
