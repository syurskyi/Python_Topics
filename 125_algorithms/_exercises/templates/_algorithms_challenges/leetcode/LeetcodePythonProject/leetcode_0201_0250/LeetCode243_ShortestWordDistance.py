'''
Created on Feb 27, 2017

@author: MT
'''

class Solution(object
    ___ shortestDistance(self, words, word1, word2
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        minLen = le.(words)
        ___ i, word __ enumerate(words
            __ word __ (word1, word2
                target = word1 __ word __ word2 else word2
                j = i+1
                w___ j < le.(words
                    __ words[j] __ target:
                        minLen = min(minLen, j-i)
                    j+=1
        r_ minLen
    
    ___ test(self
        testCases = [
            (
                ["a","c","b","a"],
                "a",
                "b",
            )
        ]
        ___ words, word1, word2 __ testCases:
            print('words: %s' % words)
            print('word1: %s' % word1)
            print('word2: %s' % word2)
            result = self.shortestDistance(words, word1, word2)
            print('result: %s' % (result))
            print('-='*20+'-')

__  -n __ '__main__':
    Solution().test()
