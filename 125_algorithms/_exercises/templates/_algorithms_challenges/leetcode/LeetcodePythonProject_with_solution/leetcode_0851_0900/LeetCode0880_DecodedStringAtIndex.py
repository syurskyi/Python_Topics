'''
Created on Oct 15, 2019

@author: tongq
'''
class Solution(object):
    ___ decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        n = 0
        for i, c in enumerate(S):
            __ c.isdigit():
                n = n*int(c)
            else:
                n += 1
        for j in range(i, -1, -1):
            c = S[j]
            __ c.isdigit():
                n //= int(c)
                K %= n
            else:
                __ K == n or K == 0:
                    return c
                n -= 1
    
    ___ decodeAtIndex_own_MLE(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        tmp = ''
        for c in S:
            __ c.isdigit():
                tmp += tmp*(int(c)-1)
            else:
                tmp += c
            __ K-1 < len(tmp):
                return tmp[K-1]
        return tmp[K-1]
