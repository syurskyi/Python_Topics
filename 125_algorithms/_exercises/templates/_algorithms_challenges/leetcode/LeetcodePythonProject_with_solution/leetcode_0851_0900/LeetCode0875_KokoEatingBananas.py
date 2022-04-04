'''
Created on Oct 7, 2019

@author: tongq
'''
c_ Solution(o..
    ___ minEatingSpeed  piles, H
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        _______ m__
        piles.s..()
        l, r = 1, m..(piles)
        w.... l <_ r:
            mid = l+(r-l)//2
            sumVal = s..(m__.c.. f__(num)/mid) ___ num __ piles)
            __ sumVal <_ H:
                r = mid-1
            ____
                l = mid+1
        r.. l
    
    ___ test
        testCases = [
            [
                [3,6,7,11],
                8
            ],
            [
                [30,11,23,4,20],
                5,
            ],
            [
                [30,11,23,4,20],
                6,
            ],
        ]
        ___ piles, h __ testCases:
            res = minEatingSpeed(piles, h)
            print('res: %s' % s..(res
            print('-='*30+'-')

__ _____ __ _____
    _______ m__
    print(m__.c.. f__(3)/3
    print(m__.c.. f__(4)/3
    Solution().test()
