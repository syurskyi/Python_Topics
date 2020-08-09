'''
Created on Feb 27, 2018

@author: tongq
'''
class Solution(object
    ___ canMeasureWater(self, x, y, z
        __ x+y<z: r_ False
        __ x __ z or y __ z or x+y __ z:
            r_ True
        w___ y != 0:
            tmp = y
            y = x%y
            x = tmp
        r_ bool(z%x__0)
