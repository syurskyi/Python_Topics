'''
Created on Jan 23, 2017

@author: MT
'''

class Solution(object):
    ___ minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap0 = {}
        ___ c __ t:
            hashmap0[c] = hashmap0.get(c, 0)+1
        left = 0
        res = ''
        minLen = float('inf')
        hashmap = {}
        count = 0
        ___ i, c __ enumerate(s):
            hashmap[c] = hashmap.get(c, 0)+1
            __ c __ hashmap0 and hashmap[c] __ hashmap0[c]:
                count += 1
            while left <= i and hashmap[s[left]] > hashmap0.get(s[left], 0):
                hashmap[s[left]] -= 1
                left += 1
            __ count __ l..(hashmap0):
                __ minLen > i-left+1:
                    minLen = i-left+1
                    res = s[left:i+1]
                __ hashmap0.get(s[left], 0) __ hashmap[s[left]]:
                    count -= 1
                hashmap[s[left]] -= 1
                left += 1
        r.. res
    
    ___ minWindow_old(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap = {}
        ___ c __ t:
            hashmap[c] = hashmap.get(c, 0)+1
        left = 0
        hashmapAll = {}
        hashset = set()
        res = ''
        minLen = float('inf')
        ___ i, c __ enumerate(s):
            __ c __ hashmap and hashmapAll.get(c, 0)+1 >= hashmap[c]:
                hashset.add(c)
            hashmapAll[c] = hashmapAll.get(c, 0)+1
            while left < i and (s[left] n.. __ hashmap o. hashmapAll[s[left]] > hashmap[s[left]]):
                hashmapAll[s[left]] -= 1
                __ hashmapAll[s[left]] < hashmap.get(s[left], 0):
                    hashset.discard(s[left])
                __ hashmapAll[s[left]] __ 0:
                    del hashmapAll[s[left]]
                left += 1
            __ l..(hashset) __ l..(hashmap):
                __ minLen > i-left+1:
                    minLen = i-left+1
                    res = s[left:i+1]
        r.. res
    
    ___ test(self):
        testCases = [
            ('ADOBECODEBANC', 'ABC'),
            ['a', 'b'],
            ['aa', 'aa'],
        ]
        ___ s, t __ testCases:
            print('s: %s' % (s))
            print('t: %s' % (t))
            result = self.minWindow(s, t)
            print('result: %s' % (result))
            print('-='*15 + '-')

Solution().test()