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
        ___ i, word __ enumerate(words):
            __ word __ [word1, word2]:
                target = word2 __ word __ word1 ____ word1
                j = i+1
                while j < l..(words):
                    __ words[j] __ target:
                        res = m..(res, j-i)
                    j += 1
        r.. res
