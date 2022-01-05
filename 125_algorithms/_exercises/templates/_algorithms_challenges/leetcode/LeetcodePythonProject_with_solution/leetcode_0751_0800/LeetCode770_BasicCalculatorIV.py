'''
Created on Apr 5, 2018

@author: tongq
'''
c_ Solution(object):
    ___ basicCalculatorIV  expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        p..
    
    ___ test
        testCases = [
            [
                "e + 8 - a + 5",
                ["e"],
                [1],
            ],
            [
                "e - 8 + temperature - pressure",
                ["e", "temperature"],
                [1, 12],
            ],
            [
                "7 - 7",
                [],
                [],
            ],
            [
                "a * b * c + b * a * c * 4",
                [],
                [],
            ],
            [
                "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
                [],
                [],
            ],
        ]
        ___ expression, evalvars, evalints __ testCases:
            result = basicCalculatorIV(expression, evalvars, evalints)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
