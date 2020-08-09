'''
Created on Mar 8, 2017

@author: MT
'''

class Solution(object
    ___ wordPatternMatch(self, pattern, s
        __ not pattern and not s: r_ True
        __ not pattern or not s: r_ False
        hashmap = {}
        r_ self.helper(pattern, s, 0, 0, hashmap, set())
         
    ___ helper(self, pattern, s, i, j, hashmap, hashset
        __ i __ le.(pattern) and j __ le.(s
            r_ True
        __ i >= le.(pattern) or j >= le.(s
            r_ False
        c = pattern[i]
        ___ k in range(j+1, le.(s)+1
            sub = s[j:k]
            __ c not in hashmap and sub not in hashset:
                hashmap[c] = sub
                hashset.add(sub)
                __ self.helper(pattern, s, i+1, k, hashmap, hashset
                    r_ True
                del hashmap[c]
                hashset.remove(sub)
            ____ c in hashmap and hashmap[c] __ sub:
                __ self.helper(pattern, s, i+1, k, hashmap, hashset
                    r_ True
        r_ False
    
    ___ test(self
        testCases = [
            ('abab', 'redblueredblue'),
            ('aaaa', 'asdasdasdasd'),
            ('aabb', 'xyzabcxzyabc'),
            ('d', 'ef'),
        ]
        ___ pattern, s in testCases:
            print('pattern: %s' % (pattern))
            print('s: %s' % (s))
            result = self.wordPatternMatch(pattern, s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
