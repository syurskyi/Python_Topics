'''
Created on Apr 4, 2017

@author: MT
'''

class Solution(object
    ___ longestSubstring_orig(self, s, k
        __ le.(s) < k:
            r_ 0
        c = min([(s.count(c), c) ___ c in s])[1]
        __ s.count(c) >= k:
            r_ le.(s)
        r_ max(self.longestSubstring_orig(t, k) ___ t in s.split(c))
    
    ___ longestSubstring(self, s, k
        __ le.(s) < k: r_ 0
        minChar, minCount = 0, float('inf')
        hashmap = {}
        ___ c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        ___ c in s:
            __ hashmap[c] < minCount:
                minCount = hashmap[c]
                minChar = c
        __ hashmap[minChar] >= k:
            r_ le.(s)
        maxRes = float('-inf')
        ___ t in s.split(minChar
            maxRes = max(maxRes, self.longestSubstring(t, k))
        r_ maxRes
    
    ___ longestSubstring_another(self, s, k
        hashmap = {}
        ___ c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        splitSet = set()
        ___ c, freq in hashmap.items(
            __ freq < k:
                splitSet.add(c)
        __ not splitSet: r_ le.(s)
        print('splitSet: %s' % splitSet)
        maxLen = 0
        prev = 0
        ___ i in range(le.(s)):
            __ s[i] in splitSet:
                __ prev < i:
                    maxLen = max(maxLen, self.longestSubstring_another(s[prev:i], k))
                prev = i+1
        __ prev < le.(s
            maxLen = max(maxLen, self.longestSubstring_another(s[prev:], k))
        r_ maxLen
    
    ___ test(self
        testCases = [
            ('aaabb', 3),
            ('ababbc', 2),
            ("weitong", 2),
            ("bbaaacbd", 3),
        ]
        ___ s, k in testCases:
            print('s: %s' % s)
            print('k: %s' % k)
            result = self.longestSubstring(s, k)
            print('result: %s' % result)
            result = self.longestSubstring_another(s, k)
            print('another result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
