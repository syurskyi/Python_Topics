'''
Created on May 1, 2018

@author: tongq
'''
c_ Solution(object):
    ___ ambiguousCoordinates  S):
        """
        :type S: str
        :rtype: List[str]
        """
        s = S
        n = l..(s)
        res    # list
        ___ i __ r..(1, n-2):
            arrA = helper(s[1:i+1])
            arrB = helper(s[i+1:n-1])
            ___ s1 __ arrA:
                ___ s2 __ arrB:
                    res.a..('(%s, %s)' % (s1, s2))
        r.. res
    
    ___ helper  s):
        n = l..(s)
        res    # list
        __ n __ 0 o. (n > 1 a.. s[0] __ '0' a.. s[-1] __ '0'):
            r.. res
        __ n > 1 a.. s[0] __ '0':
            res.a..('0.'+s[1:])
            r.. res
        res.a..(s)
        __ n __ 1 o. s[-1] __ '0':
            r.. res
        ___ i __ r..(1, n):
            res.a..(s[:i]+'.'+s[i:])
        r.. res
    
    ___ test
        testCases = [
            '(123)',
            '(00011)',
            '(0123)',
            '(100)',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = ambiguousCoordinates(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
