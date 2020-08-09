'''
Created on Feb 9, 2017

@author: MT
'''

class Solution(object
    ___ wordBreak(self, s, wordDict
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        __ not s: r_ []
        dp = [[] for _ in range(le.(s)+1)]
        dp[0] = True
        for i in range(le.(s)+1
            __ dp[i]:
                for word in wordDict:
                    __ s[i:i+le.(word)] __ word:
                        dp[i+le.(word)].append(word)
        res = []
        self.helper(dp, le.(s), res, [])
        r_ res
    
    ___ helper(self, dp, i, res, curr
        __ i <= 0:
            __ i __ 0:
                res.append(' '.join(curr))
            r_
        for word in dp[i]:
            __ i >= le.(word
                curr.insert(0, word)
                self.helper(dp, i-le.(word), res, curr)
                curr.pop(0)
    
    ___ test(self
        testCases = [
            ('catsanddog', ["cat", "cats", "and", "sand", "dog"]),
        ]
        for s, wordDict in testCases:
            print('s: %s' % (s))
            print('wordDict: %s' % (wordDict))
            result = self.wordBreak(s, wordDict)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
