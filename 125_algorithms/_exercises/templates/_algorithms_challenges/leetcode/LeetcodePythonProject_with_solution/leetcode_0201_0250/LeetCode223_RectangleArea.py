'''
Created on Feb 21, 2017

@author: MT
'''
c_ Solution(o..
    ___ computeArea  A, B, C, D, E, F, G, H
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        xA1, xA2, yA1, yA2 A, C, B, D
        xB1, xB2, yB1, yB2 E, G, F, H
        common 0
        aArea (xA2-xA1)*(yA2-yA1)
        bArea (xB2-xB1)*(yB2-yB1)
        
        __ xA1 <_ xB1 <_ xA2:
            xTmp m..(xB2, xA2)
            __ yA1 <_ yB1 < yA2:
                yTmp m..(yB2, yA2)
                common (xTmp-xB1)*(yTmp-yB1)
            ____ yB1 <_ yA1 < yB2:
                yTmp m..(yA2, yB2)
                common (xTmp-xB1)*(yTmp-yA1)
        ____ xB1 <_ xA1 <_ xB2:
            xTmp m..(xB2, xA2)
            __ yA1 <_ yB1 < yA2:
                yTmp m..(yB2, yA2)
                common (xTmp-xA1)*(yTmp-yB1)
            ____ yB1 <_ yA1 < yB2:
                yTmp m..(yA2, yB2)
                common (xTmp-xA1)*(yTmp-yA1)
        r.. aArea+bArea-common
