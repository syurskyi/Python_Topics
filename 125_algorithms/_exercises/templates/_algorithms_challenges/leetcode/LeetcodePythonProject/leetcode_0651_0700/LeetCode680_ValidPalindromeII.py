'''
Created on Oct 19, 2017

@author: MT
'''
class Solution(object
    ___ validPalindrome(self, s
        """
        :type s: str
        :rtype: bool
        """
        __ not s:
            r_ True
        i, j = 0, le.(s)-1
        w___ i < j and s[i] __ s[j]:
            i += 1
            j -= 1
        __ i >= j:
            r_ True
        i0, j0 = i, j
        i += 1
        w___ i < j and s[i] __ s[j]:
            i += 1
            j -= 1
        __ i >= j:
            r_ True
        i, j = i0, j0
        j -= 1
        w___ i < j and s[i] __ s[j]:
            i += 1
            j -= 1
        __ i >= j:
            r_ True
        r_ False
    
    ___ test(self
        testCases = [
            'aba',
            'abca',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.validPalindrome(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
