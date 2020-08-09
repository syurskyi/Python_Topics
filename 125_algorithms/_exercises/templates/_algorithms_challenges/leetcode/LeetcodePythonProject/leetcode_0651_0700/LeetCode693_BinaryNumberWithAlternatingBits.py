'''
Created on Oct 25, 2017

@author: MT
'''
class Solution(object
    ___ hasAlternatingBits(self, n
        """
        :type n: int
        :rtype: bool
        """
        prev = n&1
        n >>= 1
        w___ n > 0:
            digit = n & 1
            __ not digit ^ prev:
                r_ False
            prev = digit
            n >>= 1
        r_ True
    
    ___ test(self
        testCases = [
            4,
            5,
            7,
            11,
            10,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.hasAlternatingBits(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
