'''
Created on Sep 16, 2019

@author: tongq
'''
c_ Solution(o..
    ___ mirrorReflection  p, q
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        w.... p % 2 __ 0 a.. q % 2 __ 0:
            p, q p//2, q//2
        __ p % 2 __ 0:
            r.. 2
        ____ q % 2 __ 0:
            r.. 0
        ____
            r.. 1
    
    ___ test
        testCases [
            
        ]
        ___ p, q __ testCases:
            res mirrorReflection(p, q)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
