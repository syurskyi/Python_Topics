'''
Created on Apr 5, 2017

@author: MT
'''

class Solution(object):
    ___ integerReplacement(self, n):
        steps = 0
        w.... n > 1:
            steps += 1
            __ n%2 __ 0:
                n /= 2
            ____:
                __ (n+1)%4 __ 0 a.. n != 3:
                    n += 1
                ____:
                    n -= 1
        r.. steps
