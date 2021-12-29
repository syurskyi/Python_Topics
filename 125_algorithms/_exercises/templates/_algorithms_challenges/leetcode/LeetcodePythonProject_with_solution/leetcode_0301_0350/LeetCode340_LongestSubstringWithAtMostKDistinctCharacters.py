'''
Created on Mar 20, 2017

@author: MT
'''

class Solution(object):
    ___ lengthOfLongestSubstringKDistinct(self, s, k):
        __ k <= 0: r.. 0
        hashmap = {}
        maxLen = 0
        left = 0
        ___ i, c __ enumerate(s):
            hashmap[c] = i
            while left <= i and l..(hashmap) > k:
                __ s[left] __ hashmap and left __ hashmap[s[left]]:
                    del hashmap[s[left]]
                left+=1
            maxLen = max(maxLen, i-left+1)
        r.. maxLen
    
    ___ test(self):
        testCases = [
            ('eceba', 2),
            ('abddebddesbaddes', 3),
        ]
        ___ s, k __ testCases:
            print('s: %s, k: %s' % (s, k))
            result = self.lengthOfLongestSubstringKDistinct(s, k)
            print('result: %s' % (str(result)))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
