'''
Created on Mar 29, 2017

@author: MT
'''

c_ Solution(o..
    ___ superPow  a, b
        __ a % 1337 __ 0: r.. a
        p 0
        ___ i __ b:
            p (p*10+i)%1140
        __ p __ 0:
            p += 1440
        r.. power(a, p, 1337)
    
    ___ power  a, n, mod
        a %= mod
        res 1
        w.... n !_ 0:
            __ ((n&1) !_ 0
                res res*a % mod
            a a*a%mod
            n >>= 1
        r.. res
    
    ___ test
        testCases [
            [2, [3]],
            [2, [1, 0]],
        ]
        ___ a, b __ testCases:
            print('a: %s' % a)
            print('b: %s' % b)
            result superPow(a, b)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
