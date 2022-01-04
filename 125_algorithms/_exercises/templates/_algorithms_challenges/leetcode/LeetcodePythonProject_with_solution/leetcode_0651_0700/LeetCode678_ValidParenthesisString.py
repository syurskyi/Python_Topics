'''
Created on Oct 18, 2017

@author: MT
'''
c_ Solution(object):
    ___ checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low, high = 0, 0
        ___ c __ s:
            __ c __ '(':
                low += 1
                high += 1
            ____ c __ ')':
                __ low > 0:
                    low -= 1
                high -= 1
            ____:
                __ low > 0:
                    low -= 1
                high += 1
            __ high < 0:
                r.. F..
        r.. low __ 0
    
    ___ test
        testCases = [
            '()',
            '(*)',
            '(*))',
            '(*()',
            '(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = checkValidString(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
