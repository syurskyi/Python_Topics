'''
Created on Oct 8, 2018

@author: tongq
'''
c_ Solution(object):
    ___ isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        r.. x11 < x22 a.. x21 < x12 a.. y11 < y22 a.. y21 < y12
    
    ___ isRectangleOverlap_own(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        __ (x11 <= x21 < x12 a.. (y11 <= y21 < y12 o. y21 <= y11 < y12 <= y22)) o.\
           (x11 <= x21 < x12 a.. (y11 < y22 <= y12 o. y21 <= y11 < y12 <= y22)) o.\
           (x11 < x22 <= x12 a.. (y11 <= y21 < y12 o. y21 <= y11 < y12 <= y22)) o.\
           (x11 < x22 <= x12 a.. (y11 < y22 <= y12 o. y21 <= y11 < y12 <= y22)) o.\
           (x21 <= x11 < x22 a.. (y21 <= y11 < y22 o. y11 <= y21 < y22 <= y12)) o.\
           (x21 <= x11 < x22 a.. (y21 < y12 <= y22 o. y11 <= y21 < y22 <= y12)) o.\
           (x21 < x12 <= x22 a.. (y21 <= y11 < y22 o. y11 <= y21 < y22 <= y12)) o.\
           (x21 < x12 <= x22 a.. (y21 < y12 <= y22 o. y11 <= y21 < y22 <= y12)):
            r.. T..
        r.. F..

    ___ test
        testCases = [
            [
                [229,-132,833,333],
                [-244,-577,837,804],
            ],
            [
                [0,0,1,1],
                [1,0,2,1],
            ],
            [
                [7,8,13,15],
                [10,8,12,20],
            ],
        ]
        ___ rec1, rec2 __ testCases:
            result = isRectangleOverlap(rec1, rec2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
