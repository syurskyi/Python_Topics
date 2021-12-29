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
        s = s.replace(' ', '')
        i = 0
        res = 0
        curVal = 0
        preVal = 0
        sign = '+'
        while i < len(s):
            __ s[i].isdigit():
                curVal = 0
                while i < len(s) and s[i].isdigit():
                    curVal = curVal*10+int(s[i])
                    i += 1
            __ sign == '+':
                res += preVal
                preVal = curVal
            elif sign == '-':
                res += preVal
                preVal = -curVal
            elif sign == '*':
                preVal *= curVal
            elif sign == '/':
                __ preVal//curVal < 0 and preVal%curVal != 0:
                    preVal = preVal//curVal+1
                else:
                    preVal = preVal//curVal
            __ i < len(s):
                sign = s[i]
                i += 1
        res += preVal
        return res
    
    ___ test(self):
        testCases = [
            '3*3-5',
            '-5+3*5',
            '14-3/2',
            '14-13/2',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.calculate(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
