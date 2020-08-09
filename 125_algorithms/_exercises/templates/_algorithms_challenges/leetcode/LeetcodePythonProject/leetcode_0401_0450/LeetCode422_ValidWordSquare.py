'''
Created on Apr 13, 2017

@author: MT
'''

class Solution(object
    ___ validWordSquare(self, words
        __ not words: r_ False
        for i, word1 in enumerate(words
            word2 = ''
            for j in range(le.(word1)):
                __ j >= le.(words
                    r_ False
                __ i >= le.(words[j]
                    r_ False
                word2 += words[j][i]
            __ word1 != word2:
                r_ False
        r_ True
