'''
Created on Feb 18, 2017

@author: MT
'''
c_ Solution(o..
    ___ isIsomorphic  s, t
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap    # dict
        hashset s..()
        __ l..(s) != l..(t
            r.. F..
        ___ c1, c2 __ z..(s, t
            __ c1 n.. __ hashmap:
                __ c2 __ hashset:
                    r.. F..
                hashmap[c1] c2
                hashset.add(c2)
            ____
                __ hashmap[c1] != c2:
                    r.. F..
        r.. T..
    
    ___ isIsomorphic_old  s, t
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ l..(s) != l..(t r.. F..
        hashmap1, hashmap2    # dict, {}
        ___ c1, c2 __ z..(s, t
            __ c1 __ hashmap1 a..\
            (c2 n.. __ hashmap2 o. hashmap1[c1] != c2 o. hashmap2[c2] != c1
                r.. F..
            ____ c2 __ hashmap2 a..\
            (c1 n.. __ hashmap1 o. hashmap1[c1] != c2 o. hashmap2[c2] != c1
                r.. F..
            hashmap1[c1] c2
            hashmap2[c2] c1
        r.. T..
    
    ___ test
        testCases [
            ('ab', 'aa'),
            ('egg', 'add'),
            ('foo', 'bar'),
            ('paper', 'title'),
        ]
        ___ s, t __ testCases:
            print('s: %s, t: %s' % (s, t
            result isIsomorphic(s, t)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()