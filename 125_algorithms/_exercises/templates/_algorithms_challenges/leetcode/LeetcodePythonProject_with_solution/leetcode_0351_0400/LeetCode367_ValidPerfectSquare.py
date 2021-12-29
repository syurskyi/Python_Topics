'''
Created on Feb 27, 2018

@author: tongq
'''
class Solution(object):
    ___ isPerfectSquare(self, num):
        __ num <= 0: r.. False
        l, r = 1, num//2+1
        while l <= r:
            mid = (l+r)//2
            __ mid*mid __ num:
                r.. True
            ____ mid*mid > num:
                r = mid-1
            ____:
                l = mid+1
        r.. False
