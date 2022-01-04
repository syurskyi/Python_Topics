'''
Created on Oct 7, 2019

@author: tongq
'''
c_ Solution(object):
    ___ minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        _______ math
        piles.s..()
        l, r = 1, max(piles)
        w.... l <= r:
            mid = l+(r-l)//2
            sumVal = s..(math.ceil(float(num)/mid) ___ num __ piles)
            __ sumVal <= H:
                r = mid-1
            ____:
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
            print('res: %s' % s..(res))
            print('-='*30+'-')

__ _____ __ _____
    _______ math
    print(math.ceil(float(3)/3))
    print(math.ceil(float(4)/3))
    Solution().test()
