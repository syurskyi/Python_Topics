'''
Created on Feb 9, 2017

@author: MT
'''

c_ Solution(o..
    ___ wordBreak  s, wordDict
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        __ n.. s: r.. []
        dp = [[] ___ _ __ r..(l..(s)+1)]
        dp[0] = T..
        ___ i __ r..(l..(s)+1
            __ dp[i]:
                ___ word __ wordDict:
                    __ s[i:i+l..(word)] __ word:
                        dp[i+l..(word)].a..(word)
        res    # list
        helper(dp, l..(s), res, [])
        r.. res
    
    ___ helper  dp, i, res, curr
        __ i <_ 0:
            __ i __ 0:
                res.a..(' '.j..(curr
            r..
        ___ word __ dp[i]:
            __ i >_ l..(word
                curr.insert(0, word)
                helper(dp, i-l..(word), res, curr)
                curr.p.. 0)
    
    ___ test
        testCases = [
            ('catsanddog', ["cat", "cats", "and", "sand", "dog"]),
        ]
        ___ s, wordDict __ testCases:
            print('s: %s' % (s
            print('wordDict: %s' % (wordDict
            result = wordBreak(s, wordDict)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
