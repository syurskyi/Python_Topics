'''
Created on Sep 10, 2017

@author: MT
'''
c_ Solution(o..
    ___ smallestFactorization  a
        """
        :type a: int
        :rtype: int
        """
        __ a < 10: r.. a
        res    # list
        ___ i __ r..(9, 1, -1
            w.... a%i __ 0:
                res.a..(i)
                a //= i
        __ a >_ 10 o. n.. res: r.. 0
        result = ''
        ___ i __ r..(l..(res)-1, -1, -1
            result += s..(res[i])
        result = i..(result)
        r.. result __ result < 2**31-1 ____ 0
    
    ___ test
        testCases = [
            48,
            15,
            11,
            22,
        ]
        ___ num __ testCases:
            print('num: %s' % num)
            result = smallestFactorization(num)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
