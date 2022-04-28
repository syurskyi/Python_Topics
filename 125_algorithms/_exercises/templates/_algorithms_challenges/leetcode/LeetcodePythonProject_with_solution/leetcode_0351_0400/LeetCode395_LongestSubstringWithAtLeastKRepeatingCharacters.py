'''
Created on Apr 4, 2017

@author: MT
'''

c_ Solution(o..
    ___ longestSubstring_orig  s, k
        __ l..(s) < k:
            r.. 0
        c m..([(s.c.. c), c) ___ c __ s])[1]
        __ s.c.. c) >_ k:
            r.. l..(s)
        r.. m..(longestSubstring_orig(t, k) ___ t __ s.s..(c
    
    ___ longestSubstring  s, k
        __ l..(s) < k: r.. 0
        minChar, minCount 0, f__('inf')
        hashmap    # dict
        ___ c __ s:
            hashmap[c] hashmap.g.. c, 0)+1
        ___ c __ s:
            __ hashmap[c] < minCount:
                minCount hashmap[c]
                minChar c
        __ hashmap[minChar] >_ k:
            r.. l..(s)
        maxRes f__ '-inf'
        ___ t __ s.s..(minChar
            maxRes m..(maxRes, longestSubstring(t, k
        r.. maxRes
    
    ___ longestSubstring_another  s, k
        hashmap    # dict
        ___ c __ s:
            hashmap[c] hashmap.g.. c, 0)+1
        splitSet s..()
        ___ c, freq __ hashmap.i..
            __ freq < k:
                splitSet.add(c)
        __ n.. splitSet: r.. l..(s)
        print('splitSet: %s' % splitSet)
        maxLen 0
        prev 0
        ___ i __ r..(l..(s:
            __ s[i] __ splitSet:
                __ prev < i:
                    maxLen m..(maxLen, longestSubstring_another(s[prev:i], k
                prev i+1
        __ prev < l..(s
            maxLen m..(maxLen, longestSubstring_another(s[prev:], k
        r.. maxLen
    
    ___ test
        testCases [
            ('aaabb', 3),
            ('ababbc', 2),
            ("weitong", 2),
            ("bbaaacbd", 3),
        ]
        ___ s, k __ testCases:
            print('s: %s' % s)
            print('k: %s' % k)
            result longestSubstring(s, k)
            print('result: %s' % result)
            result longestSubstring_another(s, k)
            print('another result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
