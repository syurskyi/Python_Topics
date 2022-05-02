'''
Created on Feb 28, 2017

@author: MT
'''

c_ Solution(o..
    ___ groupStrings  strings
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashmap    # dict
        ___ s __ strings:
            hashStr getHash(s)
            hashmap[hashStr] hashmap.g.. hashStr,    # list) + [s]
        res    # list
        ___ vals __ hashmap.v..
            res.a..(vals)
        r.. res
    
    ___ getHash  s
        __ n.. s: r.. '-2'
        __ l..(s) __ 1: r.. '-1'
        res ''
        ___ i __ r..(1, l..(s:
            diff o..(s[i])-o..(s[i-1])
            __ diff < 0:
                diff += 26
            res += '%s,' % diff
        r.. res
    
    ___ groupStrings_another  strings
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        result    # list
        ___ s __ strings:
            added F..
            ___ l __ result:
                __ isSameGroup(l[0], s
                    l.a..(s)
                    added T..
            __ n.. added:
                result.a..([s])
        r.. result
    
    ___ isSameGroup  s1, s2
        __ l..(s1) !_ l..(s2
            r.. F..
        length l..(s1)
        __ length __ 1:
            r.. T..
        diff o..(s1 0 - o..(s2 0
        __ diff < 0:
            diff += 26
        ___ i __ r..(1, length
            d o..(s1[i]) - o..(s2[i])
            __ d < 0:
                d += 26
            __ d > 26:
                d -_ 26
            __ d !_ diff:
                r.. F..
        r.. T..
    
    ___ test
        testCases [
            ["abc","bcd","acef","xyz","az","ba","a","z"],
        ]
        ___ strings __ testCases:
            print('strs: %s' % (strings
            result groupStrings(strings)
            print('result: %s' % (result
            print('-='*20+'-')
    
__ _____ __ _____
    Solution().test()
