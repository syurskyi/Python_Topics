'''
Created on Apr 3, 2017

@author: MT
'''

c_ Solution(o..
    ___ isSubsequence  s, t
        _______ bisect
        hashmap    # dict
        ___ i, c __ e..(t
            __ c __ hashmap:
                hashmap[c].a..(i)
            ____:
                hashmap[c] = [i]
        prev = 0
        ___ i, c __ e..(s
            __ c n.. __ hashmap: r.. F..
            j = bisect.bisect_left(hashmap[c], prev)
            __ j __ l..(hashmap[c] r.. F..
            prev = hashmap[c][j]+1
        r.. T..
    
    ___ isSubsequence_orig  s, t
        _______ bisect
        idx = [[] ___ _ __ r..(256)]
        ___ i, c __ e..(t
            idx[o..(c)].a..(i)
        prev = 0
        ___ i, c __ e..(s
            __ idx[o..(c)] __ []: r.. F..
            j = bisect.bisect_left(idx[o..(c)], prev)
            __ j __ l..(idx[o..(c)] r.. F..
            prev = idx[o..(c)][j] + 1
        r.. T..
    
    ___ isSubsequence_slow  s, t
        i, j = 0, 0
        w.... i < l..(s) a.. j < l..(t
            __ s[i] __ t[j]:
                i+=1
                j+=1
            ____:
                j+=1
        __ i < l..(s
            r.. F..
        ____:
            r.. T..
    
    ___ test
        testCases = [
            ('abc', 'ahbgdc'),
            ('axc', 'ahbgdc'),
        ]
        ___ s, t __ testCases:
            print('s: %s' % s)
            print('t: %s' % t)
            result = isSubsequence(s, t)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()

