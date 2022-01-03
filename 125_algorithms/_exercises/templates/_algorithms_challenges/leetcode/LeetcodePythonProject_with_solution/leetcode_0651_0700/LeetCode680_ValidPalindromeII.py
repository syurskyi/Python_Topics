'''
Created on Oct 19, 2017

@author: MT
'''
c_ Solution(object):
    ___ validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        __ n.. s:
            r.. T..
        i, j = 0, l..(s)-1
        w.... i < j a.. s[i] __ s[j]:
            i += 1
            j -= 1
        __ i >= j:
            r.. T..
        i0, j0 = i, j
        i += 1
        w.... i < j a.. s[i] __ s[j]:
            i += 1
            j -= 1
        __ i >= j:
            r.. T..
        i, j = i0, j0
        j -= 1
        w.... i < j a.. s[i] __ s[j]:
            i += 1
            j -= 1
        __ i >= j:
            r.. T..
        r.. F..
    
    ___ test
        testCases = [
            'aba',
            'abca',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = validPalindrome(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
