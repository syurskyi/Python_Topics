'''
Created on Feb 27, 2018

@author: tongq
'''
class Solution(object):
    ___ canMeasureWater(self, x, y, z):
        __ x+y<z: r.. False
        __ x __ z o. y __ z o. x+y __ z:
            r.. True
        while y != 0:
            tmp = y
            y = x%y
            x = tmp
        r.. bool(z%x__0)
