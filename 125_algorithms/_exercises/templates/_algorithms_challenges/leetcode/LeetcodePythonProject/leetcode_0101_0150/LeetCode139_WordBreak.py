'''
Created on Feb 9, 2017

@author: MT
'''

class Solution(object
    ___ wordBreak(self, s, wordDict
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = [False]*(le.(s)+1)
        dp[0] = True
        ___ i in range(le.(s)):
            __ not dp[i]:
                continue
            ___ word in wordDict:
                end = i+le.(word)
                sub = s[i:end]
                __ sub __ word:
                    dp[end] = True
        r_ dp[-1]
    
    ___ test(self
        pass

__ __name__ __ '__main__':
    Solution().test()