'''
Created on Jan 23, 2017

@author: MT
'''

class Solution(object
    ___ minWindow(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap0 = {}
        ___ c in t:
            hashmap0[c] = hashmap0.get(c, 0)+1
        left = 0
        res = ''
        minLen = float('inf')
        hashmap = {}
        count = 0
        ___ i, c in enumerate(s
            hashmap[c] = hashmap.get(c, 0)+1
            __ c in hashmap0 and hashmap[c] __ hashmap0[c]:
                count += 1
            w___ left <= i and hashmap[s[left]] > hashmap0.get(s[left], 0
                hashmap[s[left]] -= 1
                left += 1
            __ count __ le.(hashmap0
                __ minLen > i-left+1:
                    minLen = i-left+1
                    res = s[left:i+1]
                __ hashmap0.get(s[left], 0) __ hashmap[s[left]]:
                    count -= 1
                hashmap[s[left]] -= 1
                left += 1
        r_ res
    
    ___ minWindow_old(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap = {}
        ___ c in t:
            hashmap[c] = hashmap.get(c, 0)+1
        left = 0
        hashmapAll = {}
        hashset = set()
        res = ''
        minLen = float('inf')
        ___ i, c in enumerate(s
            __ c in hashmap and hashmapAll.get(c, 0)+1 >= hashmap[c]:
                hashset.add(c)
            hashmapAll[c] = hashmapAll.get(c, 0)+1
            w___ left < i and (s[left] not in hashmap or hashmapAll[s[left]] > hashmap[s[left]]
                hashmapAll[s[left]] -= 1
                __ hashmapAll[s[left]] < hashmap.get(s[left], 0
                    hashset.discard(s[left])
                __ hashmapAll[s[left]] __ 0:
                    del hashmapAll[s[left]]
                left += 1
            __ le.(hashset) __ le.(hashmap
                __ minLen > i-left+1:
                    minLen = i-left+1
                    res = s[left:i+1]
        r_ res
    
    ___ test(self
        testCases = [
            ('ADOBECODEBANC', 'ABC'),
            ['a', 'b'],
            ['aa', 'aa'],
        ]
        ___ s, t in testCases:
            print('s: %s' % (s))
            print('t: %s' % (t))
            result = self.minWindow(s, t)
            print('result: %s' % (result))
            print('-='*15 + '-')

Solution().test()