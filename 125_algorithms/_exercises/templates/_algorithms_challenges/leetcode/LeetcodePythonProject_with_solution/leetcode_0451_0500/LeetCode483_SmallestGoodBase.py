'''
Created on May 3, 2017

@author: MT
'''

c_ Solution(o..
    ___ smallestGoodBase  n
        """
        :type n: str
        :rtype: str
        """
        _______ math
        n = i..(n)
        max_n = i..(math.log(n, 2))
        ___ m __ r..(max_n, 1, -1
            k = i..(n**m**-1)
            __ (k**(m+1)-1)//(k-1) __ n:
                r.. s..(k)
        r.. s..(n-1)
    
    ___ test
        testCases = [
            '13',
            '4681',
            '1000000000000000000',
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = smallestGoodBase(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
