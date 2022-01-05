'''
Created on Sep 5, 2017

@author: MT
'''

c_ Solution(object):
    ___ validSquare  p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        lengths = [
            getLen(p1, p2),
            getLen(p2, p3),
            getLen(p3, p4),
            getLen(p4, p1),
            getLen(p1, p3),
            getLen(p2, p4),
        ]
        maxVal, nonMax = 0, 0
        count = 0
        ___ length __ lengths:
            maxVal = m..(maxVal, length)
        ___ length __ lengths:
            __ maxVal != length:
                nonMax = length
            ____:
                count += 1
        __ count != 2: r.. F..
        ___ length __ lengths:
            __ nonMax != length a.. maxVal != length:
                r.. F..
        r.. T..
    
    ___ getLen  p1, p2):
        r.. (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
