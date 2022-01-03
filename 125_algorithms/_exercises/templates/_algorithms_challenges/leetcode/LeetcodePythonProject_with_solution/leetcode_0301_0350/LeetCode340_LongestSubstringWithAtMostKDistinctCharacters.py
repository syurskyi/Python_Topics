'''
Created on Mar 20, 2017

@author: MT
'''

c_ Solution(object):
    ___ lengthOfLongestSubstringKDistinct(self, s, k):
        __ k <= 0: r.. 0
        hashmap    # dict
        maxLen = 0
        left = 0
        ___ i, c __ e..(s):
            hashmap[c] = i
            w.... left <= i a.. l..(hashmap) > k:
                __ s[left] __ hashmap a.. left __ hashmap[s[left]]:
                    del hashmap[s[left]]
                left+=1
            maxLen = max(maxLen, i-left+1)
        r.. maxLen
    
    ___ test
        testCases = [
            ('eceba', 2),
            ('abddebddesbaddes', 3),
        ]
        ___ s, k __ testCases:
            print('s: %s, k: %s' % (s, k))
            result = lengthOfLongestSubstringKDistinct(s, k)
            print('result: %s' % (s..(result)))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
