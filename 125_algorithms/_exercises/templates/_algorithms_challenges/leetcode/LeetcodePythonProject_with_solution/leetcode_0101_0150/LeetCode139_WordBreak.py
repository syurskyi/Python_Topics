'''
Created on Feb 9, 2017

@author: MT
'''

c_ Solution(object):
    ___ wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = [F..]*(l..(s)+1)
        dp[0] = T..
        ___ i __ r..(l..(s)):
            __ n.. dp[i]:
                continue
            ___ word __ wordDict:
                end = i+l..(word)
                sub = s[i:end]
                __ sub __ word:
                    dp[end] = T..
        r.. dp[-1]
    
    ___ test
        pass

__ __name__ __ '__main__':
    Solution().test()