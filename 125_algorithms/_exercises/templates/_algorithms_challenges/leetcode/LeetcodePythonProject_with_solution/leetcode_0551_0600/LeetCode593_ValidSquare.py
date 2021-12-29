'''
Created on Sep 5, 2017

@author: MT
'''

class Solution(object):
    ___ validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        lengths = [
            self.getLen(p1, p2),
            self.getLen(p2, p3),
            self.getLen(p3, p4),
            self.getLen(p4, p1),
            self.getLen(p1, p3),
            self.getLen(p2, p4),
        ]
        maxVal, nonMax = 0, 0
        count = 0
        ___ length __ lengths:
            maxVal = max(maxVal, length)
        ___ length __ lengths:
            __ maxVal != length:
                nonMax = length
            ____:
                count += 1
        __ count != 2: r.. False
        ___ length __ lengths:
            __ nonMax != length and maxVal != length:
                r.. False
        r.. True
    
    ___ getLen(self, p1, p2):
        r.. (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
