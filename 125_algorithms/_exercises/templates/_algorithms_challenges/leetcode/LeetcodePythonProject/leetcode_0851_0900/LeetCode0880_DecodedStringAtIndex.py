'''
Created on Oct 15, 2019

@author: tongq
'''
class Solution(object
    ___ decodeAtIndex(self, S, K
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        n = 0
        for i, c in enumerate(S
            __ c.isdigit(
                n = n*int(c)
            ____
                n += 1
        for j in range(i, -1, -1
            c = S[j]
            __ c.isdigit(
                n //= int(c)
                K %= n
            ____
                __ K __ n or K __ 0:
                    r_ c
                n -= 1
    
    ___ decodeAtIndex_own_MLE(self, S, K
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        tmp = ''
        for c in S:
            __ c.isdigit(
                tmp += tmp*(int(c)-1)
            ____
                tmp += c
            __ K-1 < le.(tmp
                r_ tmp[K-1]
        r_ tmp[K-1]
