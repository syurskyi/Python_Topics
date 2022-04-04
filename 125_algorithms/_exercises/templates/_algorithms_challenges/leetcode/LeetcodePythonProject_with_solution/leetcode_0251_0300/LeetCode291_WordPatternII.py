'''
Created on Mar 8, 2017

@author: MT
'''

c_ Solution(o..
    ___ wordPatternMatch  pattern, s
        __ n.. pattern a.. n.. s: r.. T..
        __ n.. pattern o. n.. s: r.. F..
        hashmap    # dict
        r.. helper(pattern, s, 0, 0, hashmap, s..
         
    ___ helper  pattern, s, i, j, hashmap, hashset
        __ i __ l..(pattern) a.. j __ l..(s
            r.. T..
        __ i >_ l..(pattern) o. j >_ l..(s
            r.. F..
        c = pattern[i]
        ___ k __ r..(j+1, l..(s)+1
            sub = s[j:k]
            __ c n.. __ hashmap a.. sub n.. __ hashset:
                hashmap[c] = sub
                hashset.add(sub)
                __ helper(pattern, s, i+1, k, hashmap, hashset
                    r.. T..
                del hashmap[c]
                hashset.remove(sub)
            ____ c __ hashmap a.. hashmap[c] __ sub:
                __ helper(pattern, s, i+1, k, hashmap, hashset
                    r.. T..
        r.. F..
    
    ___ test
        testCases = [
            ('abab', 'redblueredblue'),
            ('aaaa', 'asdasdasdasd'),
            ('aabb', 'xyzabcxzyabc'),
            ('d', 'ef'),
        ]
        ___ pattern, s __ testCases:
            print('pattern: %s' % (pattern
            print('s: %s' % (s
            result = wordPatternMatch(pattern, s)
            print('result: %s' % (result
            print('-='*20+'-')
    
__ _____ __ _____
    Solution().test()
