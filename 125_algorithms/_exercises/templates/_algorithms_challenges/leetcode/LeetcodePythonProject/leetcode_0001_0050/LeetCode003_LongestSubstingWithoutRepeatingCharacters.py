'''
Created on May 5, 2017

@author: MT
'''

class Solution(object
    ___ lengthOfLongestSubstring(self, s
        """
        :type s: str
        :rtype: int
        """
        left = 0
        hashset = set()
        maxLen = 0
        for i, c in enumerate(s
            w___ left < i and c in hashset:
                hashset.discard(s[left])
                left += 1
            hashset.add(c)
            maxLen = max(maxLen, i-left+1)
        r_ maxLen
    
    ___ test(self
        testCases = [
            'abc',
            'bbbb',
            'abcdba',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.lengthOfLongestSubstring(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
