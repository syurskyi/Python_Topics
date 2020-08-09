'''
Created on May 12, 2018

@author: tongq
'''
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
___ knows(a, b
    ______ random
    r_ random(0, 1) __ 0

class Solution(object
    ___ findCelebrity(self, n
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n-1
        w___ l < r:
            __ knows(l, r
                l += 1
            ____
                r -= 1
        for i in range(n
            __ i __ l or (knows(i, l) and not knows(l, i)):
                continue
            ____
                r_ -1
        r_ l
