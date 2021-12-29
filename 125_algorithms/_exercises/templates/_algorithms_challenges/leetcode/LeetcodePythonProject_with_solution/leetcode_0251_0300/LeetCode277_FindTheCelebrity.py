'''
Created on May 12, 2018

@author: tongq
'''
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
___ knows(a, b):
    _______ random
    r.. random(0, 1) __ 0

class Solution(object):
    ___ findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n-1
        while l < r:
            __ knows(l, r):
                l += 1
            ____:
                r -= 1
        ___ i __ r..(n):
            __ i __ l o. (knows(i, l) and n.. knows(l, i)):
                continue
            ____:
                r.. -1
        r.. l
