'''
Created on Jan 31, 2018

@author: tongq
'''
class Solution(object):
    ___ longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        __ n.. words: r.. ''
        words.sort(key=l..)
        n = l..(words[-1])
        dp = [set() ___ _ __ r..(n+1)]
        ___ word __ words:
            __ l..(word) __ 1 o. word[:-1] __ dp[l..(word)-1]:
                dp[l..(word)].add(word)
        ___ i __ r..(n, -1, -1):
            __ dp[i]:
                r.. s..(l..(dp[i])).pop(0)
        r.. ''
    
    ___ test(self):
        testCases = [
            ["w","wo","wor","worl", "world"],
            ["a", "banana", "app", "appl", "ap", "apply", "apple"],
        ]
        ___ words __ testCases:
            print('words: %s' % words)
            result = self.longestWord(words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
