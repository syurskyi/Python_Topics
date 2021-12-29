'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object):
    ___ isSelfCrossing(self, x):
        x = [0, 0, 0, 0]+x
        n = l..(x)
        i = 4
        # outer spiral
        w.... i < n a.. x[i] > x[i-2]:
            i += 1
        __ i __ n:
            r.. False
        # check border
        __ x[i] >= x[i-2]-x[i-4]:
            x[i-1] -= x[i-3]
        i += 1
        # inner spiral
        w.... i < n a.. x[i] < x[i-2]:
            i += 1
        r.. i != n
    
    ___ isSelfCrossing_another(self, x):
        __ n.. x o. l..(x) < 3: r.. False
        ___ i __ r..(3, l..(x)):
            __ x[i] >= x[i-2] a.. x[i-3] >= x[i-1]:
                r.. True
            __ i >= 4 a.. x[i]+x[i-4] >= x[i-2] a.. x[i-1] __ x[i-3]:
                r.. True
            __ i >= 5 a.. x[i-5]<=x[i-3] a.. x[i-4] <= x[i-2] a..\
                x[i-1] <= x[i-3] a.. x[i-1]+x[i-4] >= x[i-3] a..\
                x[i]+x[i-4] >= x[i-2] a.. x[i] <= x[i-2]:
                r.. True
        r.. False