'''
Created on Oct 18, 2017

@author: MT
'''
class Solution(object):
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
                r.. False
        r.. low __ 0
    
    ___ test(self):
        testCases = [
            '()',
            '(*)',
            '(*))',
            '(*()',
            '(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.checkValidString(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
