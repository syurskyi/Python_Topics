'''
Created on May 3, 2017

@author: MT
'''

class Solution(object):
    ___ smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        import math
        n = int(n)
        max_n = int(math.log(n, 2))
        for m in range(max_n, 1, -1):
            k = int(n**m**-1)
            __ (k**(m+1)-1)//(k-1) == n:
                return str(k)
        return str(n-1)
    
    ___ test(self):
        testCases = [
            '13',
            '4681',
            '1000000000000000000',
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.smallestGoodBase(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
