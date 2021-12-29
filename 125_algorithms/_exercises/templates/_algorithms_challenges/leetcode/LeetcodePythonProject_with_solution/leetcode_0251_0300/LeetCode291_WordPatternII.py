'''
Created on Mar 8, 2017

@author: MT
'''

class Solution(object):
    ___ wordPatternMatch(self, pattern, s):
        __ n.. pattern a.. n.. s: r.. True
        __ n.. pattern o. n.. s: r.. False
        hashmap = {}
        r.. self.helper(pattern, s, 0, 0, hashmap, set())
         
    ___ helper(self, pattern, s, i, j, hashmap, hashset):
        __ i __ l..(pattern) a.. j __ l..(s):
            r.. True
        __ i >= l..(pattern) o. j >= l..(s):
            r.. False
        c = pattern[i]
        ___ k __ r..(j+1, l..(s)+1):
            sub = s[j:k]
            __ c n.. __ hashmap a.. sub n.. __ hashset:
                hashmap[c] = sub
                hashset.add(sub)
                __ self.helper(pattern, s, i+1, k, hashmap, hashset):
                    r.. True
                del hashmap[c]
                hashset.remove(sub)
            ____ c __ hashmap a.. hashmap[c] __ sub:
                __ self.helper(pattern, s, i+1, k, hashmap, hashset):
                    r.. True
        r.. False
    
    ___ test(self):
        testCases = [
            ('abab', 'redblueredblue'),
            ('aaaa', 'asdasdasdasd'),
            ('aabb', 'xyzabcxzyabc'),
            ('d', 'ef'),
        ]
        ___ pattern, s __ testCases:
            print('pattern: %s' % (pattern))
            print('s: %s' % (s))
            result = self.wordPatternMatch(pattern, s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
