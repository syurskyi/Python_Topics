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
        __ n.. s: r.. []
        dp = [[] ___ _ __ r..(l..(s)+1)]
        dp[0] = True
        ___ i __ r..(l..(s)+1):
            __ dp[i]:
                ___ word __ wordDict:
                    __ s[i:i+l..(word)] __ word:
                        dp[i+l..(word)].a..(word)
        res    # list
        self.helper(dp, l..(s), res, [])
        r.. res
    
    ___ helper(self, dp, i, res, curr):
        __ i <= 0:
            __ i __ 0:
                res.a..(' '.join(curr))
            r..
        ___ word __ dp[i]:
            __ i >= l..(word):
                curr.insert(0, word)
                self.helper(dp, i-l..(word), res, curr)
                curr.pop(0)
    
    ___ test(self):
        testCases = [
            ('catsanddog', ["cat", "cats", "and", "sand", "dog"]),
        ]
        ___ s, wordDict __ testCases:
            print('s: %s' % (s))
            print('wordDict: %s' % (wordDict))
            result = self.wordBreak(s, wordDict)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
