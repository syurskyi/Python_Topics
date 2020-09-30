'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object
    ___ mySqrt(self, x
        """
        :type x: int
        :rtype: int
        """
        start, end = 1, x
        w___ start <= end:
            mid = (start+end)/2
            __ mid*mid __ x:
                r_ mid
            ____ mid*mid < x:
                start = mid+1
            ____
                end = mid-1
        r_ start __ start __ 0 else start-1
    
    ___ test(self
        pass

__  -n __ '__main__':
    Solution().test()