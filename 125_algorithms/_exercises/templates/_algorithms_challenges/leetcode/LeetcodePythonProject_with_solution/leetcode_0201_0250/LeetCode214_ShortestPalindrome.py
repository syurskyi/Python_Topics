'''
Created on Feb 19, 2017

@author: MT
'''

c_ Solution(object):
    ___ shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, l..(s)-1
        w.... j >= 0:
            __ s[i] __ s[j]:
                i += 1
            j -= 1
        __ i __ l..(s):
            r.. s
        mid = s[:i]
        suffix = s[i:]
        r.. suffix[::-1]+shortestPalindrome(mid)+suffix
    
    ___ test
        testCases = [
            'aacecaaa',
            'abcd',
            'aacecabccaa',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = shortestPalindrome(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
