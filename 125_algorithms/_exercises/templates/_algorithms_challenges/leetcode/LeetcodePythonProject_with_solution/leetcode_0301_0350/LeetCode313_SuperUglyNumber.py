'''
Created on Mar 15, 2017

@author: MT
'''

class Solution(object):
    ___ nthSuperUglyNumber(self, n, primes):
        times = [0]*l..(primes)
        res = [1]
        ___ _ __ r..(n-1):
            minVal = float('inf')
            ___ i, p __ z..(times, primes):
                minVal = m..(minVal, res[i]*p)
            res.a..(minVal)
            ___ i __ r..(l..(times)):
                __ minVal __ res[times[i]]*primes[i]:
                    times[i] += 1
        r.. res[-1]
