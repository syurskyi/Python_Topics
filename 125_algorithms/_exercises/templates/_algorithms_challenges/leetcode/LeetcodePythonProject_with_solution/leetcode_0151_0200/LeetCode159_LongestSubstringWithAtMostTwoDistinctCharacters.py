'''
Created on May 22, 2018

@author: tongq
'''
c_ Solution(o..
    ___ lengthOfLongestSubstringTwoDistinct  s
        """
        :type s: str
        :rtype: int
        """
        hashmap    # dict
        l = 0
        res = 0
        ___ i, c __ e..(s
            hashmap[c] = hashmap.g.. c, 0)+1
            w.... l..(hashmap) > 2:
                hashmap[s[l]] -= 1
                __ hashmap[s[l]] __ 0: del hashmap[s[l]]
                l += 1
            res = m..(res, i-l+1)
        res = m..(res, l..(s)-l)
        r.. res
    
    ___ test
        testCases = [
            'abccccbbb',
            'eceba',
            'abc',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = lengthOfLongestSubstringTwoDistinct(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
