'''
Created on Feb 27, 2018

@author: tongq
'''
c_ Solution(object):
    ___ isPerfectSquare(self, num):
        __ num <= 0: r.. F..
        l, r = 1, num//2+1
        w.... l <= r:
            mid = (l+r)//2
            __ mid*mid __ num:
                r.. T..
            ____ mid*mid > num:
                r = mid-1
            ____:
                l = mid+1
        r.. F..
