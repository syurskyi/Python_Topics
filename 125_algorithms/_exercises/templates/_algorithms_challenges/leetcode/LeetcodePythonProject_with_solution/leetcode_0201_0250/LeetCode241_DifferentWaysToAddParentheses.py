'''
Created on Feb 27, 2017

@author: MT
'''

class Solution(object):
    ___ diffWaysToCompute(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res    # list
        ___ i, c __ enumerate(s):
            __ c __ ('+', '-', '*'):
                res1 = self.diffWaysToCompute(s[:i])
                res2 = self.diffWaysToCompute(s[i+1:])
                ___ num1 __ res1:
                    ___ num2 __ res2:
                        __ c __ '+':
                            res.a..(num1+num2)
                        ____ c __ '-':
                            res.a..(num1-num2)
                        ____:
                            res.a..(num1*num2)
        __ n.. res:
            res = [int(s)]
        r.. res
    
    ___ test(self):
        testCases = [
            '2-1-1',
            '2*3-4*5',
        ]
        ___ s __ testCases:
            print('input: %s' % s)
            result = self.diffWaysToCompute(s)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
