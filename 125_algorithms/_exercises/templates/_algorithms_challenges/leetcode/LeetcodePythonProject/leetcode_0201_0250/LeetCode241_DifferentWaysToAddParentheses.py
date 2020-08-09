'''
Created on Feb 27, 2017

@author: MT
'''

class Solution(object
    ___ diffWaysToCompute(self, s
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        for i, c in enumerate(s
            __ c in ('+', '-', '*'
                res1 = self.diffWaysToCompute(s[:i])
                res2 = self.diffWaysToCompute(s[i+1:])
                for num1 in res1:
                    for num2 in res2:
                        __ c __ '+':
                            res.append(num1+num2)
                        ____ c __ '-':
                            res.append(num1-num2)
                        ____
                            res.append(num1*num2)
        __ not res:
            res = [int(s)]
        r_ res
    
    ___ test(self
        testCases = [
            '2-1-1',
            '2*3-4*5',
        ]
        for s in testCases:
            print('input: %s' % s)
            result = self.diffWaysToCompute(s)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
