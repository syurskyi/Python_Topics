'''
Created on Feb 18, 2017

@author: MT
'''

class Solution(object):
    ___ rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        __ m __ 0:
            r.. 0
        moveFactor = 1
        w.... m != n:
            m >>= 1
            n >>= 1
            moveFactor <<= 1
        r.. moveFactor*m
    
    ___ test(self):
        testCases = [
            (5, 7),
            (5, 20),
            (3, 7),
            (101, 110),
        ]
        ___ m, n __ testCases:
            print('m: %s, n: %s' % (m, n))
            result = self.rangeBitwiseAnd(m, n)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
    