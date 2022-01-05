'''
Created on Mar 19, 2017

@author: MT
'''

c_ Solution(o..):
    ___ isSelfCrossing  x):
        x = [0, 0, 0, 0]+x
        n = l..(x)
        i = 4
        # outer spiral
        w.... i < n a.. x[i] > x[i-2]:
            i += 1
        __ i __ n:
            r.. F..
        # check border
        __ x[i] >= x[i-2]-x[i-4]:
            x[i-1] -= x[i-3]
        i += 1
        # inner spiral
        w.... i < n a.. x[i] < x[i-2]:
            i += 1
        r.. i != n
    
    ___ isSelfCrossing_another  x):
        __ n.. x o. l..(x) < 3: r.. F..
        ___ i __ r..(3, l..(x)):
            __ x[i] >= x[i-2] a.. x[i-3] >= x[i-1]:
                r.. T..
            __ i >= 4 a.. x[i]+x[i-4] >= x[i-2] a.. x[i-1] __ x[i-3]:
                r.. T..
            __ i >= 5 a.. x[i-5]<=x[i-3] a.. x[i-4] <= x[i-2] a..\
                x[i-1] <= x[i-3] a.. x[i-1]+x[i-4] >= x[i-3] a..\
                x[i]+x[i-4] >= x[i-2] a.. x[i] <= x[i-2]:
                r.. T..
        r.. F..