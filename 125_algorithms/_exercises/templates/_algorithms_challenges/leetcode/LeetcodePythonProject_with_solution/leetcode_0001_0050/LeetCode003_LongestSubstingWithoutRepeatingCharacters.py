'''
Created on May 5, 2017

@author: MT
'''

c_ Solution(object):
    ___ lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        hashset = set()
        maxLen = 0
        ___ i, c __ e..(s):
            w.... left < i a.. c __ hashset:
                hashset.discard(s[left])
                left += 1
            hashset.add(c)
            maxLen = max(maxLen, i-left+1)
        r.. maxLen
    
    ___ test
        testCases = [
            'abc',
            'bbbb',
            'abcdba',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = lengthOfLongestSubstring(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
