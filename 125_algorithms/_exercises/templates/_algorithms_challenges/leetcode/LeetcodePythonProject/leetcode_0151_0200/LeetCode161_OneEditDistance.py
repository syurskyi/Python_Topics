'''
Created on Feb 12, 2017

@author: MT
'''

class Solution(object
    ___ isOneEditDistance(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ s is None or t is None:
            r_ False
        m, n = le.(t), le.(s)
        __ abs(m-n) > 1:
            r_ False
        i, j, count = 0, 0, 0
        w___ i < n and j < m:
            __ s[i] __ t[j]:
                i+=1
                j+=1
            ____
                count+=1
                __ count>1:
                    r_ False
                __ m>n:
                    j+=1
                ____ n>m:
                    i+=1
                ____
                    i+=1
                    j+=1
        __ i < n or j < m:
            count += 1
        __ count __ 1:
            r_ True
        r_ False
    
    ___ test(self
        pass

__ __name__ __ '__main__':
    Solution().test()
