'''
Created on Apr 10, 2017

@author: MT
'''

c_ Solution(o..
    ___ toHex  num
        __ num __ 0: r.. '0'
        mp '0123456789abcdef'
        result ''
        ___ _ __ r..(8
            c mp[num&15]
            result c + result
            num >>= 4
        r.. result.l..('0')
    
    ___ test
        testCases [
            26,
            -1,
        ]
        ___ num __ testCases:
            print('num: %s' % num)
            result toHex(num)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
