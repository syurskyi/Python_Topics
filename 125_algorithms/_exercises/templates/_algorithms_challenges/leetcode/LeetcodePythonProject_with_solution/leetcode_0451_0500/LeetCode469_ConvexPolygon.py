'''
Created on Apr 25, 2017

@author: MT
'''

c_ Solution(object):
    ___ isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        gotNegative, gotPositive = F.., F..
        length = l..(points)
        ___ i __ r..(length):
            a = points[i-1]
            b = points[i]
            c = points[(i+1)%length]
            crossProduct = crossProductLength(a[0], a[1], b[0], b[1], c[0], c[1])
            __ crossProduct < 0:
                gotNegative = T..
            ____ crossProduct > 0:
                gotPositive = T..
            __ gotNegative a.. gotPositive: r.. F..
        r.. T..
    
    ___ crossProductLength(self, ax, ay, bx, by, cx, cy):
        bax = ax-bx
        bay = ay-by
        bcx = cx-bx
        bcy = cy-by
        r.. (bax*bcy-bay*bcx)
