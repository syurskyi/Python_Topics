'''
Created on Mar 20, 2017

@author: MT
'''

class Solution(object
    ___ lengthOfLongestSubstringKDistinct(self, s, k
        __ k <= 0: r_ 0
        hashmap = {}
        maxLen = 0
        left = 0
        ___ i, c __ enumerate(s
            hashmap[c] = i
            w___ left <= i and le.(hashmap) > k:
                __ s[left] __ hashmap and left __ hashmap[s[left]]:
                    del hashmap[s[left]]
                left+=1
            maxLen = ma.(maxLen, i-left+1)
        r_ maxLen
    
    ___ test(self
        testCases = [
            ('eceba', 2),
            ('abddebddesbaddes', 3),
        ]
        ___ s, k __ testCases:
            print('s: %s, k: %s' % (s, k))
            result = self.lengthOfLongestSubstringKDistinct(s, k)
            print('result: %s' % (str(result)))
            print('-='*20+'-')

__  -n __ '__main__':
    Solution().test()
