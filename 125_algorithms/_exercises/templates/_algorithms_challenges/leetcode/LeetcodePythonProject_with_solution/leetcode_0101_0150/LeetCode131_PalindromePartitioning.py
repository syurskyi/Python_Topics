'''
Created on Feb 8, 2017

@author: MT
'''
c_ Solution(o..):
    ___ partition  s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result    # list
        __ n.. s: r.. result
        helper(s, 0, [], result)
        r.. result
    
    ___ helper  s, startInd, elem, result):
        __ startInd __ l..(s):
            result.a..(l..(elem))
            r..
        ___ i __ r..(startInd, l..(s)):
            __ isPalindrome(s[startInd:i+1]):
                elem.a..(s[startInd:i+1])
                helper(s, i+1, elem, result)
                elem.pop()
    
    ___ isPalindrome  s):
        __ n.. s: r.. F..
        start, end = 0, l..(s)-1
        w.... start<=end:
            __ s[start] != s[end]:
                r.. F..
            start += 1
            end -= 1
        r.. T..
    
    ___ test
        testCases = [
            'aab',
            'aabbcc',
            'abcba',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = partition(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()