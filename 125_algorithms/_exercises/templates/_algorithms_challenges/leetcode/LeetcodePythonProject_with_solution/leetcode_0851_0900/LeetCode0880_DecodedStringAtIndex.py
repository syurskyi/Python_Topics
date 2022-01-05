'''
Created on Oct 15, 2019

@author: tongq
'''
c_ Solution(object):
    ___ decodeAtIndex  S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        n = 0
        ___ i, c __ e..(S):
            __ c.isdigit
                n = n*i..(c)
            ____:
                n += 1
        ___ j __ r..(i, -1, -1):
            c = S[j]
            __ c.isdigit
                n //= i..(c)
                K %= n
            ____:
                __ K __ n o. K __ 0:
                    r.. c
                n -= 1
    
    ___ decodeAtIndex_own_MLE  S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        tmp = ''
        ___ c __ S:
            __ c.isdigit
                tmp += tmp*(i..(c)-1)
            ____:
                tmp += c
            __ K-1 < l..(tmp):
                r.. tmp[K-1]
        r.. tmp[K-1]
