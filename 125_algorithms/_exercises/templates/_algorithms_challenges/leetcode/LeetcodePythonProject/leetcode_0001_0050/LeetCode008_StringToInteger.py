'''
Created on Nov 8, 2017

@author: MT
'''
class Solution(object
    ___ myAtoi(self, str
        """
        :type str: str
        :rtype: int
        """
        s = str
        s = s.strip()
        __ not s or s __ '+': r_ 0
        sig = 1
        __ s[0] __ '+':
            s = s[1:]
        ____ s[0] __ '-':
            s = s[1:]
            sig = -1
        s = s.lstrip('0')
        res = 0
        for c in s:
            __ not c.isdigit(
                break
            res = 10*res + ord(c) - ord('0') 
        __ sig > 0:
            r_ min(2**32-1, res)
        ____
            r_ max(-2**31, sig*res)
    
    ___ test(self
        testCases = [
            '    010',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.myAtoi(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
