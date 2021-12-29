'''
Created on Feb 8, 2017

@author: MT
'''
class Solution(object):
    ___ partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result    # list
        __ n.. s: r.. result
        self.helper(s, 0, [], result)
        r.. result
    
    ___ helper(self, s, startInd, elem, result):
        __ startInd __ l..(s):
            result.a..(l..(elem))
            r..
        ___ i __ r..(startInd, l..(s)):
            __ self.isPalindrome(s[startInd:i+1]):
                elem.a..(s[startInd:i+1])
                self.helper(s, i+1, elem, result)
                elem.pop()
    
    ___ isPalindrome(self, s):
        __ n.. s: r.. False
        start, end = 0, l..(s)-1
        while start<=end:
            __ s[start] != s[end]:
                r.. False
            start += 1
            end -= 1
        r.. True
    
    ___ test(self):
        testCases = [
            'aab',
            'aabbcc',
            'abcba',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = self.partition(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()