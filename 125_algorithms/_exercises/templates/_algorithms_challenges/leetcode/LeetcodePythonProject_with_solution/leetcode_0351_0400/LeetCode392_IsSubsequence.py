'''
Created on Apr 3, 2017

@author: MT
'''

class Solution(object):
    ___ isSubsequence(self, s, t):
        import bisect
        hashmap = {}
        for i, c in enumerate(t):
            __ c in hashmap:
                hashmap[c].append(i)
            else:
                hashmap[c] = [i]
        prev = 0
        for i, c in enumerate(s):
            __ c not in hashmap: return False
            j = bisect.bisect_left(hashmap[c], prev)
            __ j == len(hashmap[c]): return False
            prev = hashmap[c][j]+1
        return True
    
    ___ isSubsequence_orig(self, s, t):
        import bisect
        idx = [[] for _ in range(256)]
        for i, c in enumerate(t):
            idx[ord(c)].append(i)
        prev = 0
        for i, c in enumerate(s):
            __ idx[ord(c)] == []: return False
            j = bisect.bisect_left(idx[ord(c)], prev)
            __ j == len(idx[ord(c)]): return False
            prev = idx[ord(c)][j] + 1
        return True
    
    ___ isSubsequence_slow(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            __ s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        __ i < len(s):
            return False
        else:
            return True
    
    ___ test(self):
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

__ __name__ == '__main__':
    Solution().test()

