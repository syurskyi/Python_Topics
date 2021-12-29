'''
Created on Oct 13, 2019

@author: tongq
'''
class Solution(object):
    ___ nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        n, a, b = N, A, B
        while b:
            a, b = b, a%b
        l, r, lcm = 2, 10**14, A*B // a
        while l < r:
            m = (l+r)//2
            __ m // A + m // B - m // lcm < n:
                l = m+1
            ____:
                r = m
        r.. l % (10**9+7)
    
    ___ test(self):
        testCases = [
            [5, 2, 4],
        ]
        ___ n, a, b __ testCases:
            res = self.nthMagicalNumber(n, a, b)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
