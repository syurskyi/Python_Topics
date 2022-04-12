'''
Created on Apr 2, 2018

@author: tongq
'''
c_ Solution(o..
    ___ countPrimeSetBits  L, R
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes s..([2, 3, 5, 7, 11, 13, 17, 19])
        cnt 0
        ___ num __ r..(L, R+1
            bits 0
            n num
            w.... n > 0
                bits += n & 1
                n >>= 1
            cnt += 1 __ bits __ primes ____ 0
        r.. cnt
    
    ___ test
        testCases [
            [6, 10],
            [10, 15],
            [942063, 945851],
        ]
        ___ l, r __ testCases:
            print('l: %s' % l)
            print('r: %s' % r)
            result countPrimeSetBits(l, r)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
