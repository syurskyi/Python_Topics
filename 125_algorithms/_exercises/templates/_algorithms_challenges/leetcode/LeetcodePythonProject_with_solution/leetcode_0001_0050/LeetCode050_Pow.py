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
        __ n == 0:
            return 1
        __ n < 0:
            n = -n
            x = 1/x
        __ n%2==0:
            return self.myPow(x*x, n/2)
        else:
            return x*self.myPow(x*x, n/2)
    
    ___ test(self):
        pass

__ __name__ == '__main__':
    Solution().test()