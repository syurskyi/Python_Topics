'''
Created on Oct 22, 2017

@author: MT
'''
c_ Solution(o..
    ___ repeatedStringMatch  A, B
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        s1, s2 A, B
        n1, n2 l..(s1), l..(s2)
        k n2//n1+2
        __ s..(s1*k).c.. s2)__0:
            r.. -1
        w.... k >_ 1 a.. s..(s1*k).c.. s2)!=0:
            k -_ 1
        r.. k+1
    
    ___ test
        testCases [
            [
                'abcd',
                'cdabcdab',
            ]
        ]
        ___ A, B __ testCases:
            print('A: %s' % A)
            print('B: %s' % B)
            result repeatedStringMatch(A, B)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
