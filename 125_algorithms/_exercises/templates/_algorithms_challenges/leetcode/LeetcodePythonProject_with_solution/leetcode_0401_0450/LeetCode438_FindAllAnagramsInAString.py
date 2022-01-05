'''
Created on Apr 17, 2017

@author: MT
'''

c_ Solution(o..):
    ___ findAnagrams  s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        arr0 = [0]*26
        ___ c __ p:
            arr0[o..(c)-o..('a')] += 1
        left = 0
        res    # list
        arr = [0]*26
        ___ i, c __ e..(s):
            arr[o..(c)-o..('a')] += 1
            w.... left <= i a.. arr[o..(c)-o..('a')] > arr0[o..(c)-o..('a')]:
                arr[o..(s[left])-o..('a')] -= 1
                left += 1
            __ i-left+1 __ l..(p):
                res.a..(left)
        r.. res
    
    ___ findAnagrams_orig  s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        arr0 = [0]*26
        count = l..(p)
        ___ c __ p:
            arr0[o..(c)-o..('a')] += 1
        left = 0
        arr1 = [0]*26
        result    # list
        end = 0
        w.... end < l..(s):
            numInd = o..(s[end]) - o..('a')
            __ arr1[numInd] < arr0[numInd]:
                arr1[numInd] += 1
                count -= 1
                end += 1
                __ count __ 0:
                    result.a..(left)
            ____:
                arr1[o..(s[left]) - o..('a')] -= 1
                count += 1
                left += 1
        r.. result
    
    ___ test
        testCases = [
            ('cbaebabacd', 'abc'),
            ('abab', 'ab'),
        ]
        ___ s, p __ testCases:
            result = findAnagrams(s, p)
            print('result: %s' % result)
            result0 = findAnagrams_orig(s, p)
            print('result0: %s' % result0)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
