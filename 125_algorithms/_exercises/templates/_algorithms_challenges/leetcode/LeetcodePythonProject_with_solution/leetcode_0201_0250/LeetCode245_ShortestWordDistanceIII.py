'''
Created on May 14, 2018

@author: tongq
'''
class Solution(object):
    ___ shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = float('inf')
        for i, word in enumerate(words):
            __ word in [word1, word2]:
                target = word2 __ word == word1 else word1
                j = i+1
                while j < len(words):
                    __ words[j] == target:
                        res = min(res, j-i)
                    j += 1
        return res
