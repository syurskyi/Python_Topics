'''
Created on Jun 3, 2018

@author: tongq
'''
class Solution(object
    ___ climbStairs(self, n
        """
        :type n: int
        :rtype: int
        """
        __ n <= 0: r_ 0
        __ n __ 1: r_ 1
        p1, p2 = 2, 1
        for _ in range(2, n
            curr = p1+p2
            p2 = p1
            p1 = curr
        r_ p1
