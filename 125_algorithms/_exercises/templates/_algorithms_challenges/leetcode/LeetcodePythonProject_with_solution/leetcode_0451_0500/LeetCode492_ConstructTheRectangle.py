'''
Created on May 8, 2017

@author: MT
'''

c_ Solution(object):
    ___ constructRectangle  area):
        """
        :type area: int
        :rtype: List[int]
        """
        _______ math
        l = i..(math.sqrt(area))
        w.... l < area:
            __ area%l __ 0:
                r.. [m..(l, area/l), m..(l, area/l)]
            ____:
                l += 1
        r.. [area, 1]
