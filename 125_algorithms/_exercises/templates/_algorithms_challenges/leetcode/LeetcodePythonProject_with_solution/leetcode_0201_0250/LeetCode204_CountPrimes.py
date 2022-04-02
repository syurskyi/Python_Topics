'''
Created on Feb 18, 2017

@author: MT
'''

c_ Solution(o..
    ___ countPrimes  n
        """
        :type n: int
        :rtype: int
        """
        notPrime = [F..]*(n)
        count = 0
        ___ i __ r..(2, n
            __ n.. notPrime[i]:
                count += 1
                j = 2
                w.... i*j < n:
                    notPrime[i*j] = T..
                    j += 1
        r.. count
    
    ___ countPrimesSqrt  n
        """
        :type n: int
        :rtype: int
        """
        _______ math
        __ n <= 2:
            r.. 0
        primes = [F..,]*2 + [T..,]*(n-2)
        ___ i __ r..(2, i..(math.sqrt(n-1))+1
            __ primes[i]:
                ___ j __ r..(i+i, n, i
                    primes[j] = F..
        count = 0
        ___ i __ r..(2, n
            __ primes[i]: count += 1
        print(primes)
        r.. count
    
    ___ test
        testCases = [
            6,
        ]
        ___ n __ testCases:
            print('n: %s' % (n))
            result = countPrimes(n)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
