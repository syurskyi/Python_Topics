'''
Created on Mar 15, 2017

@author: MT
'''

class Solution(object
    ___ nthSuperUglyNumber(self, n, primes
        times = [0]*le.(primes)
        res = [1]
        ___ _ in range(n-1
            minVal = float('inf')
            ___ i, p in zip(times, primes
                minVal = min(minVal, res[i]*p)
            res.append(minVal)
            ___ i in range(le.(times)):
                __ minVal __ res[times[i]]*primes[i]:
                    times[i] += 1
        r_ res[-1]
