'''
Created on Jan 21, 2017

@author: MT
'''

class Solution(object):
    ___ myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        __ n __ 0:
            r.. 1
        __ n < 0:
            n = -n
            x = 1/x
        __ n%2__0:
            r.. self.myPow(x*x, n/2)
        ____:
            r.. x*self.myPow(x*x, n/2)
    
    ___ test(self):
        pass

__ __name__ __ '__main__':
    Solution().test()