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
        __ s is None or t is None:
            return False
        m, n = len(t), len(s)
        __ abs(m-n) > 1:
            return False
        i, j, count = 0, 0, 0
        while i < n and j < m:
            __ s[i] == t[j]:
                i+=1
                j+=1
            else:
                count+=1
                __ count>1:
                    return False
                __ m>n:
                    j+=1
                elif n>m:
                    i+=1
                else:
                    i+=1
                    j+=1
        __ i < n or j < m:
            count += 1
        __ count == 1:
            return True
        return False
    
    ___ test(self):
        pass

__ __name__ == '__main__':
    Solution().test()
