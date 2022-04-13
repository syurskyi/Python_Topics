'''
Created on Sep 5, 2017

@author: MT
'''
c_ Solution(o..
    ___ fractionAddition  expression
        """
        :type expression: str
        :rtype: str
        """
        _______ __
        ints m.. i.., __.f..('[+-]?\d+', expression
        A, B 0, 1
        ___ a __ ints:
            b next(ints)
            A A*b + a*B
            B *= b
            g gcd(A, B)
            A //= g
            B //= g
        r.. '%s/%s' % (A, B)
    
    ___ gcd  a, b
        __ a __ 0:
            r.. a..(b)
        ____
            r.. gcd(b%a, a)
    
    ___ test
        testCases [
            '-1/2+1/2',
            '-1/2+1/2+1/3',
            '1/3-1/2',
            '5/3+1/3',
        ]
        ___ expression __ testCases:
            print('expression: %s' % expression)
            result fractionAddition(expression)
            print('result: %s' % result)

__ _____ __ _____
    Solution().test()
