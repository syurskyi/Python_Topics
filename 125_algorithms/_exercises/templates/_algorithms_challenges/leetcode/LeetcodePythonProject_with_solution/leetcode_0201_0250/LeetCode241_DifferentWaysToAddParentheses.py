'''
Created on Feb 27, 2017

@author: MT
'''

c_ Solution(o..
    ___ diffWaysToCompute  s
        """
        :type s: str
        :rtype: List[int]
        """
        res    # list
        ___ i, c __ e..(s
            __ c __ ('+', '-', '*'
                res1 diffWaysToCompute(s[:i])
                res2 diffWaysToCompute(s[i+1:])
                ___ num1 __ res1:
                    ___ num2 __ res2:
                        __ c __ '+':
                            res.a..(num1+num2)
                        ____ c __ '-':
                            res.a..(num1-num2)
                        ____
                            res.a..(num1*num2)
        __ n.. res:
            res [i..(s)]
        r.. res
    
    ___ test
        testCases [
            '2-1-1',
            '2*3-4*5',
        ]
        ___ s __ testCases:
            print('input: %s' % s)
            result diffWaysToCompute(s)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
