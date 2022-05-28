'''
Created on Mar 19, 2017

@author: MT
'''

c_ Solution(o..
    ___ palindromePairs  words
        __ n.. words: r..    # list
        hashmap    # dict
        result    # list
        ___ i, word __ e..(words
            hashmap[word] i
        ___ i, word __ e..(words
            ___ j __ r..(l.. ?+1
                s1 word[:j]
                s2 word[j:]
                __ isPalindrome(s1
                    str2rvs s2[::-1]
                    __ str2rvs __ hashmap a.. hashmap[str2rvs] !_ i:
                        result.a..([hashmap[str2rvs], i])
                __ isPalindrome(s2
                    str1rvs s1[::-1]
                    __ str1rvs __ hashmap a.. hashmap[str1rvs] !_ i a.. s2:
                        result.a..([i, hashmap[str1rvs]])
        r.. ?
    
    ___ isPalindrome  s
        left, right 0, l..(s)-1
        w.... left < right:
            __ s[left] !_ s[right]:
                r.. F..
            left+=1
            right-_1
        r.. T..
    
    ___ test
        testCases [
            ["bat", "tab", "cat"],
            ["abcd", "dcba", "lls", "s", "sssll"],
        ]
        ___ words __ testCases:
            print('words: %s' % (words
            result palindromePairs(words)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()

