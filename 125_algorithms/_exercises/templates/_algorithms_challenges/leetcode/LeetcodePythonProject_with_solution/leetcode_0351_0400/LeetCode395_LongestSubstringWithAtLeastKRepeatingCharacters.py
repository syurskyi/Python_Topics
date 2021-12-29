'''
Created on Apr 4, 2017

@author: MT
'''

class Solution(object):
    ___ longestSubstring_orig(self, s, k):
        __ l..(s) < k:
            r.. 0
        c = m..([(s.c.. c), c) ___ c __ s])[1]
        __ s.c.. c) >= k:
            r.. l..(s)
        r.. max(self.longestSubstring_orig(t, k) ___ t __ s.s..(c))
    
    ___ longestSubstring(self, s, k):
        __ l..(s) < k: r.. 0
        minChar, minCount = 0, float('inf')
        hashmap = {}
        ___ c __ s:
            hashmap[c] = hashmap.get(c, 0)+1
        ___ c __ s:
            __ hashmap[c] < minCount:
                minCount = hashmap[c]
                minChar = c
        __ hashmap[minChar] >= k:
            r.. l..(s)
        maxRes = float('-inf')
        ___ t __ s.s..(minChar):
            maxRes = max(maxRes, self.longestSubstring(t, k))
        r.. maxRes
    
    ___ longestSubstring_another(self, s, k):
        hashmap = {}
        ___ c __ s:
            hashmap[c] = hashmap.get(c, 0)+1
        splitSet = set()
        ___ c, freq __ hashmap.items():
            __ freq < k:
                splitSet.add(c)
        __ n.. splitSet: r.. l..(s)
        print('splitSet: %s' % splitSet)
        maxLen = 0
        prev = 0
        ___ i __ r..(l..(s)):
            __ s[i] __ splitSet:
                __ prev < i:
                    maxLen = max(maxLen, self.longestSubstring_another(s[prev:i], k))
                prev = i+1
        __ prev < l..(s):
            maxLen = max(maxLen, self.longestSubstring_another(s[prev:], k))
        r.. maxLen
    
    ___ test(self):
        testCases = [
            ('aaabb', 3),
            ('ababbc', 2),
            ("weitong", 2),
            ("bbaaacbd", 3),
        ]
        ___ s, k __ testCases:
            print('s: %s' % s)
            print('k: %s' % k)
            result = self.longestSubstring(s, k)
            print('result: %s' % result)
            result = self.longestSubstring_another(s, k)
            print('another result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
