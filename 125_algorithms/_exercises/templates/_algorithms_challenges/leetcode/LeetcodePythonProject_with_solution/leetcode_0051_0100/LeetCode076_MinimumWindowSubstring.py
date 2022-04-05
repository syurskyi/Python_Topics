'''
Created on Jan 23, 2017

@author: MT
'''

c_ Solution(o..
    ___ minWindow  s, t
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap0    # dict
        ___ c __ t:
            hashmap0[c] = hashmap0.g.. c, 0)+1
        left = 0
        res = ''
        minLen = f__('inf')
        hashmap    # dict
        count = 0
        ___ i, c __ e..(s
            hashmap[c] = hashmap.g.. c, 0)+1
            __ c __ hashmap0 a.. hashmap[c] __ hashmap0[c]:
                count += 1
            w.... left <_ i a.. hashmap[s[left]] > hashmap0.g.. s[left], 0
                hashmap[s[left]] -_ 1
                left += 1
            __ count __ l..(hashmap0
                __ minLen > i-left+1:
                    minLen = i-left+1
                    res = s[left:i+1]
                __ hashmap0.g.. s[left], 0) __ hashmap[s[left]]:
                    count -_ 1
                hashmap[s[left]] -_ 1
                left += 1
        r.. res
    
    ___ minWindow_old  s, t
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap    # dict
        ___ c __ t:
            hashmap[c] = hashmap.g.. c, 0)+1
        left = 0
        hashmapAll    # dict
        hashset = s..()
        res = ''
        minLen = f__('inf')
        ___ i, c __ e..(s
            __ c __ hashmap a.. hashmapAll.g.. c, 0)+1 >_ hashmap[c]:
                hashset.add(c)
            hashmapAll[c] = hashmapAll.g.. c, 0)+1
            w.... left < i a.. (s[left] n.. __ hashmap o. hashmapAll[s[left]] > hashmap[s[left]]
                hashmapAll[s[left]] -_ 1
                __ hashmapAll[s[left]] < hashmap.g.. s[left], 0
                    hashset.discard(s[left])
                __ hashmapAll[s[left]] __ 0:
                    del hashmapAll[s[left]]
                left += 1
            __ l..(hashset) __ l..(hashmap
                __ minLen > i-left+1:
                    minLen = i-left+1
                    res = s[left:i+1]
        r.. res
    
    ___ test
        testCases = [
            ('ADOBECODEBANC', 'ABC'),
             'a', 'b' ,
             'aa', 'aa' ,
        ]
        ___ s, t __ testCases:
            print('s: %s' % (s
            print('t: %s' % (t
            result = minWindow(s, t)
            print('result: %s' % (result
            print('-='*15 + '-')

Solution().test()