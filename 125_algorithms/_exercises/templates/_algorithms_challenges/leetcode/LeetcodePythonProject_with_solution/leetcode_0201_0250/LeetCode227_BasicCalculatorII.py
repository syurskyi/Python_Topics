'''
Created on Feb 22, 2017

@author: MT
'''
class Solution(object):
    ___ calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.r..(' ', '')
        i = 0
        res = 0
        curVal = 0
        preVal = 0
        sign = '+'
        w.... i < l..(s):
            __ s[i].isdigit():
                curVal = 0
                w.... i < l..(s) a.. s[i].isdigit():
                    curVal = curVal*10+int(s[i])
                    i += 1
            __ sign __ '+':
                res += preVal
                preVal = curVal
            ____ sign __ '-':
                res += preVal
                preVal = -curVal
            ____ sign __ '*':
                preVal *= curVal
            ____ sign __ '/':
                __ preVal//curVal < 0 a.. preVal%curVal != 0:
                    preVal = preVal//curVal+1
                ____:
                    preVal = preVal//curVal
            __ i < l..(s):
                sign = s[i]
                i += 1
        res += preVal
        r.. res
    
    ___ test(self):
        testCases = [
            '3*3-5',
            '-5+3*5',
            '14-3/2',
            '14-13/2',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = self.calculate(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
