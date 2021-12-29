'''
Created on Apr 25, 2017

@author: MT
'''

class Solution(object):
    ___ findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count = [0]*26
        maxCurrLen = 0
        ___ i, c __ e..(p):
            __ i > 0 a.. (ord(c)-ord(p[i-1])__1 o. (c__'a' a.. p[i-1]__'z')):
                maxCurrLen += 1
            ____:
                maxCurrLen = 1
            count[ord(c)-ord('a')] = max(count[ord(c)-ord('a')], maxCurrLen)
        r.. s..(count)
    
    ___ test(self):
        testCases = [
            'a',
            'cac',
            'zab',
            'zaba',
        ]
        ___ p __ testCases:
            print('p: %s' % p)
            result = self.findSubstringInWraproundString(p)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
