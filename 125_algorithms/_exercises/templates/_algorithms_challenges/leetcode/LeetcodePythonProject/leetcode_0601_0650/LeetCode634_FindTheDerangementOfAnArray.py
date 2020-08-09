'''
Created on Sep 24, 2017

@author: MT
'''
class Solution(object
    ___ findDerangement(self, n
        """
        :type n: int
        :rtype: int
        """
        dn1, dn2 = 1, 0
        __ n <= 1: r_ 0
        res = 1
        ___ i in range(3, n+1
            res = ((i-1)*(dn1+dn2))%(10**9+7)
            dn2 = dn1
            dn1 = res
        r_ int(res)
    
    ___ test(self
        testCases = [
            1,
            2,
            3,
            4,
            10,
        ]
        ___ n in testCases:
            print('n: %s' % n)
            result = self.findDerangement(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
