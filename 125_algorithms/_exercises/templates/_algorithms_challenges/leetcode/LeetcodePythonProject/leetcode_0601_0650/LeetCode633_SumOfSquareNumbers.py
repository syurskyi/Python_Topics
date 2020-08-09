'''
Created on Sep 24, 2017

@author: MT
'''

class Solution(object
    ___ judgeSquareSum(self, c
        """
        :type c: int
        :rtype: bool
        """
        ______ ma__
        __ c < 0: r_ False
        l, r = 0, int(ma__.sqrt(c))
        w___ l <= r:
            __ l*l + r*r < c:
                l += 1
            ____ l*l + r*r > c:
                r -= 1
            ____
                r_ True
        r_ False
    
    ___ test(self
        testCases = [
            0,
            3,
            4,
            5,
        ]
        ___ c in testCases:
            print(c)
            result = self.judgeSquareSum(c)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
