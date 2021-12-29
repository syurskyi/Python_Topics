'''
Created on Apr 13, 2017

@author: MT
'''

class Solution(object):
    ___ validWordSquare(self, words):
        __ not words: return False
        for i, word1 in enumerate(words):
            word2 = ''
            for j in range(len(word1)):
                __ j >= len(words):
                    return False
                __ i >= len(words[j]):
                    return False
                word2 += words[j][i]
            __ word1 != word2:
                return False
        return True
