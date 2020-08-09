'''
Created on Apr 2, 2018

@author: tongq
'''
class Solution(object
    ___ countPrimeSetBits(self, L, R
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        cnt = 0
        ___ num in range(L, R+1
            bits = 0
            n = num
            w___ n > 0:
                bits += n & 1
                n >>= 1
            cnt += 1 __ bits in primes else 0
        r_ cnt
    
    ___ test(self
        testCases = [
            [6, 10],
            [10, 15],
            [942063, 945851],
        ]
        ___ l, r in testCases:
            print('l: %s' % l)
            print('r: %s' % r)
            result = self.countPrimeSetBits(l, r)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
