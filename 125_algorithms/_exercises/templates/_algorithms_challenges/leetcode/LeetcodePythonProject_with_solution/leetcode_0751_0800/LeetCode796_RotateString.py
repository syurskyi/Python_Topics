'''
Created on Apr 18, 2018

@author: tongq
'''
c_ Solution(object):
    ___ rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        s1, s2 = A, B
        __ l..(s1) != l..(s2):
            r.. F..
        __ s1 __ s2: r.. T..
        ___ i __ r..(l..(s1)):
            __ s1[i:] + s1[:i] __ s2:
                r.. T..
        r.. F..
    
    ___ test
        testCases = [
            ['abcde', 'cdeab'],
            ['abcde', 'abced'],
        ]
        ___ s1, s2 __ testCases:
            print('s1: %s' % s1)
            print('s2: %s' % s2)
            result = rotateString(s1, s2)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
