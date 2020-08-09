'''
Created on Feb 19, 2017

@author: MT
'''

class Solution(object
    ___ shortestPalindrome(self, s
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, le.(s)-1
        w___ j >= 0:
            __ s[i] __ s[j]:
                i += 1
            j -= 1
        __ i __ le.(s
            r_ s
        mid = s[:i]
        suffix = s[i:]
        r_ suffix[::-1]+self.shortestPalindrome(mid)+suffix
    
    ___ test(self
        testCases = [
            'aacecaaa',
            'abcd',
            'aacecabccaa',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.shortestPalindrome(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
