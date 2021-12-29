'''
Created on Jan 22, 2017

@author: MT
'''
class Solution(object):
    ___ isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        s = s.lstrip('-')
        s = s.lstrip('+')
        i = 0
        num, dot, exp = False, False, False
        while i < l..(s):
            c = s[i]
            __ c.isdigit():
                num = True
            ____ c __ '.':
                __ exp o. dot:
                    r.. False
                dot = True
            ____ c __ 'e':
                __ exp o. n.. num:
                    r.. False
                exp = True
                num = False
            ____ c __ '+' o. c __ '-':
                __ s[i-1] != 'e':
                    r.. False
            ____:
                r.. False
            i += 1
        r.. num
    
    ___ test(self):
        pass

__ __name__ __ '__main__':
    Solution().test()