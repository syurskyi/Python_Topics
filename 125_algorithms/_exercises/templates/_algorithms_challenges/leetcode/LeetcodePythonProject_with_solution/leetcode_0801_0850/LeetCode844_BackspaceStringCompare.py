'''
Created on Mar 18, 2019

@author: tongq
'''
c_ Solution(o..
    ___ backspaceCompare  S, T
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s, t S, T
        s0, t0 '', ''
        ___ c __ s:
            __ c __ '#':
                s0 s0[:-1]
            ____
                s0 += c
        ___ c __ t:
            __ c __ '#':
                t0 t0[:-1]
            ____
                t0 += c
        r.. s0 __ t0
    
    ___ test
        testCases [
            
        ]
        ___ s, t __ testCases:
            result backspaceCompare(s, t)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
