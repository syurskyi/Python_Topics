'''
Created on Apr 8, 2017

@author: MT
'''

c_ Solution(o..
    ___ removeKdigits  num, k
        n l..(num)
        longest n-k
        __ k >_ n: r.. '0'
        stack    # list
        ___ c __ num:
            w.... k > 0 a.. stack a.. stack[-1] > c:
                stack.p.. )
                k -_ 1
            stack.a..(c)
        stack stack[:longest]
        res ''.j..(stack)
        res res.l..('0')
        r.. res __ res ____ '0'
    
    ___ test
        testCases [
            ("1432219", 3),
            ("10200", 1),
            ("10", 2),
            ("112", 1),
            ("1234567890", 9),
            ("1173", 2),
        ]
        ___ num, k __ testCases:
            print('num: %s' % num)
            print('k: %s' % k)
            result removeKdigits(num, k)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
