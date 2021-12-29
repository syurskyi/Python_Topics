'''
Created on Feb 27, 2017

@author: MT
'''

class Solution(object):
    ___ shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        minLen = len(words)
        for i, word in enumerate(words):
            __ word in (word1, word2):
                target = word1 __ word == word2 else word2
                j = i+1
                while j < len(words):
                    __ words[j] == target:
                        minLen = min(minLen, j-i)
                    j+=1
        return minLen
    
    ___ test(self):
        testCases = [
            (
                ["a","c","b","a"],
                "a",
                "b",
            )
        ]
        for words, word1, word2 in testCases:
            print('words: %s' % words)
            print('word1: %s' % word1)
            print('word2: %s' % word2)
            result = self.shortestDistance(words, word1, word2)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
