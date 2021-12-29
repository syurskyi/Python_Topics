'''
Created on Feb 9, 2017

@author: MT
'''

class Solution(object):
    ___ wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        __ not s: return []
        dp = [[] for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1):
            __ dp[i]:
                for word in wordDict:
                    __ s[i:i+len(word)] == word:
                        dp[i+len(word)].append(word)
        res = []
        self.helper(dp, len(s), res, [])
        return res
    
    ___ helper(self, dp, i, res, curr):
        __ i <= 0:
            __ i == 0:
                res.append(' '.join(curr))
            return
        for word in dp[i]:
            __ i >= len(word):
                curr.insert(0, word)
                self.helper(dp, i-len(word), res, curr)
                curr.pop(0)
    
    ___ test(self):
        testCases = [
            ('catsanddog', ["cat", "cats", "and", "sand", "dog"]),
        ]
        for s, wordDict in testCases:
            print('s: %s' % (s))
            print('wordDict: %s' % (wordDict))
            result = self.wordBreak(s, wordDict)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
