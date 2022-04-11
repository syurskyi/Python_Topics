'''
Created on May 31, 2018

@author: tongq
'''
c_ Solution(o..
    ___ grayCode  n
        """
        :type n: int
        :rtype: List[int]
        """
        __ n __ 0: r.. [n]
        res grayCode(n-1)
        toAdd 1 << (n-1)
        ___ i __ r..(l..(res)-1, -1, -1
            res.a..(toAdd+res[i])
        r.. res
