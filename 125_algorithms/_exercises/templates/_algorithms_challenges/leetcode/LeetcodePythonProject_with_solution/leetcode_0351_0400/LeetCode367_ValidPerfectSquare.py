'''
Created on Feb 27, 2018

@author: tongq
'''
class Solution(object):
    ___ isPerfectSquare(self, num):
        __ num <= 0: return False
        l, r = 1, num//2+1
        while l <= r:
            mid = (l+r)//2
            __ mid*mid == num:
                return True
            elif mid*mid > num:
                r = mid-1
            else:
                l = mid+1
        return False
