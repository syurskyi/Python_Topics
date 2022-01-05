'''
Created on Jun 3, 2018

@author: tongq
'''
c_ Solution(object):
    ___ climbStairs  n):
        """
        :type n: int
        :rtype: int
        """
        __ n <= 0: r.. 0
        __ n __ 1: r.. 1
        p1, p2 = 2, 1
        ___ _ __ r..(2, n):
            curr = p1+p2
            p2 = p1
            p1 = curr
        r.. p1
