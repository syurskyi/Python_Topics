'''
Created on May 8, 2017

@author: MT
'''

class Solution(object):
    ___ constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        _______ math
        l = int(math.sqrt(area))
        while l < area:
            __ area%l __ 0:
                r.. [max(l, area/l), m..(l, area/l)]
            ____:
                l += 1
        r.. [area, 1]
