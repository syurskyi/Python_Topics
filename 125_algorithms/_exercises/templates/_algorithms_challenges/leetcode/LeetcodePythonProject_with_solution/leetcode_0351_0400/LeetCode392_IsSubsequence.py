'''
Created on Apr 3, 2017

@author: MT
'''

class Solution(object):
    ___ isSubsequence(self, s, t):
        _______ bisect
        hashmap = {}
        ___ i, c __ e..(t):
            __ c __ hashmap:
                hashmap[c].a..(i)
            ____:
                hashmap[c] = [i]
        prev = 0
        ___ i, c __ e..(s):
            __ c n.. __ hashmap: r.. False
            j = bisect.bisect_left(hashmap[c], prev)
            __ j __ l..(hashmap[c]): r.. False
            prev = hashmap[c][j]+1
        r.. True
    
    ___ isSubsequence_orig(self, s, t):
        _______ bisect
        idx = [[] ___ _ __ r..(256)]
        ___ i, c __ e..(t):
            idx[ord(c)].a..(i)
        prev = 0
        ___ i, c __ e..(s):
            __ idx[ord(c)] __ []: r.. False
            j = bisect.bisect_left(idx[ord(c)], prev)
            __ j __ l..(idx[ord(c)]): r.. False
            prev = idx[ord(c)][j] + 1
        r.. True
    
    ___ isSubsequence_slow(self, s, t):
        i, j = 0, 0
        w.... i < l..(s) a.. j < l..(t):
            __ s[i] __ t[j]:
                i+=1
                j+=1
            ____:
                j+=1
        __ i < l..(s):
            r.. False
        ____:
            r.. True
    
    ___ test(self):
        testCases = [
            ('abc', 'ahbgdc'),
            ('axc', 'ahbgdc'),
        ]
        ___ s, t __ testCases:
            print('s: %s' % s)
            print('t: %s' % t)
            result = self.isSubsequence(s, t)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

