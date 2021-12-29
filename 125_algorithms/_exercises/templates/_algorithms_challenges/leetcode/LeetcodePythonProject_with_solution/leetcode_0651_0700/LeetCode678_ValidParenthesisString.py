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
        for c in s:
            __ c == '(':
                low += 1
                high += 1
            elif c == ')':
                __ low > 0:
                    low -= 1
                high -= 1
            else:
                __ low > 0:
                    low -= 1
                high += 1
            __ high < 0:
                return False
        return low == 0
    
    ___ test(self):
        testCases = [
            '()',
            '(*)',
            '(*))',
            '(*()',
            '(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.checkValidString(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
