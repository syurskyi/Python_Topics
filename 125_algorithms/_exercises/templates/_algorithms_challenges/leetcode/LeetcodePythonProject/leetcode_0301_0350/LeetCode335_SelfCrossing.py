'''
Created on Mar 19, 2017

@author: MT
'''

class Solution(object
    ___ isSelfCrossing(self, x
        x = [0, 0, 0, 0]+x
        n = le.(x)
        i = 4
        # outer spiral
        w___ i < n and x[i] > x[i-2]:
            i += 1
        __ i __ n:
            r_ False
        # check border
        __ x[i] >= x[i-2]-x[i-4]:
            x[i-1] -= x[i-3]
        i += 1
        # inner spiral
        w___ i < n and x[i] < x[i-2]:
            i += 1
        r_ i != n
    
    ___ isSelfCrossing_another(self, x
        __ not x or le.(x) < 3: r_ False
        ___ i in range(3, le.(x)):
            __ x[i] >= x[i-2] and x[i-3] >= x[i-1]:
                r_ True
            __ i >= 4 and x[i]+x[i-4] >= x[i-2] and x[i-1] __ x[i-3]:
                r_ True
            __ i >= 5 and x[i-5]<=x[i-3] and x[i-4] <= x[i-2] and\
                x[i-1] <= x[i-3] and x[i-1]+x[i-4] >= x[i-3] and\
                x[i]+x[i-4] >= x[i-2] and x[i] <= x[i-2]:
                r_ True
        r_ False