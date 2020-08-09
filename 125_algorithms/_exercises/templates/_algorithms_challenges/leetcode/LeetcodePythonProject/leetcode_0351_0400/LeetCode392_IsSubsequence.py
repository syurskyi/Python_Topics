'''
Created on Apr 3, 2017

@author: MT
'''

class Solution(object
    ___ isSubsequence(self, s, t
        ______ bisect
        hashmap = {}
        for i, c in enumerate(t
            __ c in hashmap:
                hashmap[c].append(i)
            ____
                hashmap[c] = [i]
        prev = 0
        for i, c in enumerate(s
            __ c not in hashmap: r_ False
            j = bisect.bisect_left(hashmap[c], prev)
            __ j __ le.(hashmap[c] r_ False
            prev = hashmap[c][j]+1
        r_ True
    
    ___ isSubsequence_orig(self, s, t
        ______ bisect
        idx = [[] for _ in range(256)]
        for i, c in enumerate(t
            idx[ord(c)].append(i)
        prev = 0
        for i, c in enumerate(s
            __ idx[ord(c)] __ []: r_ False
            j = bisect.bisect_left(idx[ord(c)], prev)
            __ j __ le.(idx[ord(c)] r_ False
            prev = idx[ord(c)][j] + 1
        r_ True
    
    ___ isSubsequence_slow(self, s, t
        i, j = 0, 0
        w___ i < le.(s) and j < le.(t
            __ s[i] __ t[j]:
                i+=1
                j+=1
            ____
                j+=1
        __ i < le.(s
            r_ False
        ____
            r_ True
    
    ___ test(self
        testCases = [
            ('abc', 'ahbgdc'),
            ('axc', 'ahbgdc'),
        ]
        for s, t in testCases:
            print('s: %s' % s)
            print('t: %s' % t)
            result = self.isSubsequence(s, t)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

