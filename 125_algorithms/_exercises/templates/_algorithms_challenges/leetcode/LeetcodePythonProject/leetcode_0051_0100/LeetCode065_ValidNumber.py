'''
Created on Jan 22, 2017

@author: MT
'''
class Solution(object
    ___ isNumber(self, s
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        s = s.lstrip('-')
        s = s.lstrip('+')
        i = 0
        num, dot, exp = False, False, False
        w___ i < le.(s
            c = s[i]
            __ c.isdigit(
                num = True
            ____ c __ '.':
                __ exp or dot:
                    r_ False
                dot = True
            ____ c __ 'e':
                __ exp or not num:
                    r_ False
                exp = True
                num = False
            ____ c __ '+' or c __ '-':
                __ s[i-1] != 'e':
                    r_ False
            ____
                r_ False
            i += 1
        r_ num
    
    ___ test(self
        pass

__ __name__ __ '__main__':
    Solution().test()