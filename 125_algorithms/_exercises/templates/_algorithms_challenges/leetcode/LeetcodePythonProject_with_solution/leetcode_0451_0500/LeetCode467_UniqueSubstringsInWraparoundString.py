'''
Created on Apr 25, 2017

@author: MT
'''

c_ Solution(o..
    ___ findSubstringInWraproundString  p
        """
        :type p: str
        :rtype: int
        """
        count [0]*26
        maxCurrLen 0
        ___ i, c __ e..(p
            __ i > 0 a.. (o..(c)-o..(p[i-1])__1 o. (c__'a' a.. p[i-1]__'z':
                maxCurrLen += 1
            ____
                maxCurrLen 1
            count[o..(c)-o..('a')] m..(count[o..(c)-o..('a')], maxCurrLen)
        r.. s..(count)
    
    ___ test
        testCases [
            'a',
            'cac',
            'zab',
            'zaba',
        ]
        ___ p __ testCases:
            print('p: %s' % p)
            result findSubstringInWraproundString(p)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
