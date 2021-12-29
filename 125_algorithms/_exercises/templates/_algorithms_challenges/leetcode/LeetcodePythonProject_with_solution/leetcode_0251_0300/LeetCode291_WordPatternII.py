'''
Created on Mar 8, 2017

@author: MT
'''

class Solution(object):
    ___ wordPatternMatch(self, pattern, s):
        __ not pattern and not s: return True
        __ not pattern or not s: return False
        hashmap = {}
        return self.helper(pattern, s, 0, 0, hashmap, set())
         
    ___ helper(self, pattern, s, i, j, hashmap, hashset):
        __ i == len(pattern) and j == len(s):
            return True
        __ i >= len(pattern) or j >= len(s):
            return False
        c = pattern[i]
        for k in range(j+1, len(s)+1):
            sub = s[j:k]
            __ c not in hashmap and sub not in hashset:
                hashmap[c] = sub
                hashset.add(sub)
                __ self.helper(pattern, s, i+1, k, hashmap, hashset):
                    return True
                del hashmap[c]
                hashset.remove(sub)
            elif c in hashmap and hashmap[c] == sub:
                __ self.helper(pattern, s, i+1, k, hashmap, hashset):
                    return True
        return False
    
    ___ test(self):
        testCases = [
            ('abab', 'redblueredblue'),
            ('aaaa', 'asdasdasdasd'),
            ('aabb', 'xyzabcxzyabc'),
            ('d', 'ef'),
        ]
        for pattern, s in testCases:
            print('pattern: %s' % (pattern))
            print('s: %s' % (s))
            result = self.wordPatternMatch(pattern, s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ == '__main__':
    Solution().test()
