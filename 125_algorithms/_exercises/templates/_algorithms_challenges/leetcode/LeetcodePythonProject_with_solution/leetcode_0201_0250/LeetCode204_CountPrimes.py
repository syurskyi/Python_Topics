'''
Created on Feb 18, 2017

@author: MT
'''

class Solution(object):
    ___ countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        notPrime = [False]*(n)
        count = 0
        for i in range(2, n):
            __ not notPrime[i]:
                count += 1
                j = 2
                while i*j < n:
                    notPrime[i*j] = True
                    j += 1
        return count
    
    ___ countPrimesSqrt(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        __ n <= 2:
            return 0
        primes = [False,]*2 + [True,]*(n-2)
        for i in range(2, int(math.sqrt(n-1))+1):
            __ primes[i]:
                for j in range(i+i, n, i):
                    primes[j] = False
        count = 0
        for i in range(2, n):
            __ primes[i]: count += 1
        print(primes)
        return count
    
    ___ test(self):
        testCases = [
            6,
        ]
        for n in testCases:
            print('n: %s' % (n))
            result = self.countPrimes(n)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
