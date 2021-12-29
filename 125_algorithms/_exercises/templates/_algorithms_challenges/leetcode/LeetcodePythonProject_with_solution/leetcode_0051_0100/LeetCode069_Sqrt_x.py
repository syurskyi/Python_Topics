'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    ___ mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 1, x
        while start <= end:
            mid = (start+end)/2
            __ mid*mid == x:
                return mid
            elif mid*mid < x:
                start = mid+1
            else:
                end = mid-1
        return start __ start == 0 else start-1
    
    ___ test(self):
        pass

__ __name__ == '__main__':
    Solution().test()