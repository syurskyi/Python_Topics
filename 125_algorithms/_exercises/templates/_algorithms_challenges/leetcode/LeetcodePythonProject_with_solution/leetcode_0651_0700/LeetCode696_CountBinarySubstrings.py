'''
Created on Oct 25, 2017

@author: MT
'''
c_ Solution(o..
    ___ countBinarySubstrings  s
        """
        :type s: str
        :rtype: int
        """
        __ n.. s: r.. 0
        res = 0
        i = 0
        ind = i
        w.... i+1 < l..(s) a.. s[i+1] __ s[ind]:
            i += 1
        prev = i+1-ind
        i += 1
        w.... i < l..(s
            ind = i
            w.... i+1 < l..(s) a.. s[i+1] __ s[ind]:
                i += 1
            curr = i+1-ind
            res += m..(curr, prev)
            prev = curr
            i += 1
        r.. res
    
    ___ test
        testCases = [
#             '00110011',
#             '10101',
            "00100",
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = countBinarySubstrings(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
