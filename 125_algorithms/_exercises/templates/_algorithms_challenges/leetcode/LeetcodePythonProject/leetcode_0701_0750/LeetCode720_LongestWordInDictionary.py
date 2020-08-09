'''
Created on Jan 31, 2018

@author: tongq
'''
class Solution(object
    ___ longestWord(self, words
        """
        :type words: List[str]
        :rtype: str
        """
        __ not words: r_ ''
        words.sort(key=le.)
        n = le.(words[-1])
        dp = [set() ___ _ in range(n+1)]
        ___ word in words:
            __ le.(word) __ 1 or word[:-1] in dp[le.(word)-1]:
                dp[le.(word)].add(word)
        ___ i in range(n, -1, -1
            __ dp[i]:
                r_ sorted(list(dp[i])).pop(0)
        r_ ''
    
    ___ test(self
        testCases = [
            ["w","wo","wor","worl", "world"],
            ["a", "banana", "app", "appl", "ap", "apply", "apple"],
        ]
        ___ words in testCases:
            print('words: %s' % words)
            result = self.longestWord(words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
