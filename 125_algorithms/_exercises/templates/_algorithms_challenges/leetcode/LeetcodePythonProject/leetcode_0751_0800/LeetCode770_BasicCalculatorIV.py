'''
Created on Apr 5, 2018

@author: tongq
'''
class Solution(object
    ___ basicCalculatorIV(self, expression, evalvars, evalints
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        pass
    
    ___ test(self
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
                  # list,
                  # list,
            ],
            [
                "a * b * c + b * a * c * 4",
                  # list,
                  # list,
            ],
            [
                "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
                  # list,
                  # list,
            ],
        ]
        ___ expression, evalvars, evalints __ testCases:
            result = self.basicCalculatorIV(expression, evalvars, evalints)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
