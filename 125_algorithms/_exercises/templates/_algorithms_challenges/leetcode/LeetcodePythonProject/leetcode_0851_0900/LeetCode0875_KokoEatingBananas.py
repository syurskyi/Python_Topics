'''
Created on Oct 7, 2019

@author: tongq
'''
class Solution(object
    ___ minEatingSpeed(self, piles, H
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        ______ ma__
        piles.sort()
        l, r = 1, ma.(piles)
        w___ l <= r:
            mid = l+(r-l)//2
            sumVal = su.(ma__.ceil(float(num)/mid) ___ num __ piles)
            __ sumVal <= H:
                r = mid-1
            ____
                l = mid+1
        r_ l
    
    ___ test(self
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
            res = self.minEatingSpeed(piles, h)
            print('res: %s' % str(res))
            print('-='*30+'-')

__  -n __ '__main__':
    ______ ma__
    print(ma__.ceil(float(3)/3))
    print(ma__.ceil(float(4)/3))
    Solution().test()
