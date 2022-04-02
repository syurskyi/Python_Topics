'''
Created on Feb 9, 2017

@author: MT
'''

c_ Solution(o..
    ___ wordBreak  s, wordDict
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = s..(wordDict)
        dp = [F..]*(l..(s)+1)
        dp[0] = T..
        ___ i __ r..(l..(s)):
            __ n.. dp[i]:
                _____
            ___ word __ wordDict:
                end = i+l..(word)
                sub = s[i:end]
                __ sub __ word:
                    dp[end] = T..
        r.. dp[-1]
    
    ___ test
        p..

__ _____ __ _____
    Solution().test()