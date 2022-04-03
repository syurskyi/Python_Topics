'''
Created on Oct 24, 2017

@author: MT
'''
c_ Solution(o..
    ___ topKFrequent  words, k
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hashmap    # dict
        ___ word __ words:
            hashmap[word] = hashmap.g.. word, 0)+1
        n = l..(words)
        dp = [[] ___ _ __ r..(n+1)]
        ___ word, freq __ hashmap.i..:
            dp[freq].a..(word)
        res    # list
        ___ i __ r..(n, -1, -1
            __ dp[i]:
                dp[i].s..()
                res += dp[i]
                __ l..(res) >= k:
                    _____
        r.. res[:k]
    
    ___ test
        testCases = [
            [
                ["i", "love", "leetcode", "i", "love", "coding"],
                2,
            ],
            [
                ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                4
            ],
        ]
        ___ words, k __ testCases:
            print('words: %s' % words)
            print('k: %s' % k)
            result = topKFrequent(words, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
