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
        ___ i __ r..(2, n):
            __ n.. notPrime[i]:
                count += 1
                j = 2
                w.... i*j < n:
                    notPrime[i*j] = True
                    j += 1
        r.. count
    
    ___ countPrimesSqrt(self, n):
        """
        :type n: int
        :rtype: int
        """
        _______ math
        __ n <= 2:
            r.. 0
        primes = [False,]*2 + [True,]*(n-2)
        ___ i __ r..(2, int(math.sqrt(n-1))+1):
            __ primes[i]:
                ___ j __ r..(i+i, n, i):
                    primes[j] = False
        count = 0
        ___ i __ r..(2, n):
            __ primes[i]: count += 1
        print(primes)
        r.. count
    
    ___ test(self):
        testCases = [
            6,
        ]
        ___ n __ testCases:
            print('n: %s' % (n))
            result = self.countPrimes(n)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
