'''
Created on May 8, 2017

@author: MT
'''

class Solution(object
    ___ constructRectangle(self, area
        """
        :type area: int
        :rtype: List[int]
        """
        ______ ma__
        l = int(ma__.sqrt(area))
        w___ l < area:
            __ area%l __ 0:
                r_ [max(l, area/l), min(l, area/l)]
            ____
                l += 1
        r_ [area, 1]
