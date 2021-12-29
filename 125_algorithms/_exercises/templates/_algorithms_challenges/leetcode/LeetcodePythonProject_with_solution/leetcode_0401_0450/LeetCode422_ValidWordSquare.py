'''
Created on Apr 13, 2017

@author: MT
'''

class Solution(object):
    ___ validWordSquare(self, words):
        __ n.. words: r.. False
        ___ i, word1 __ e..(words):
            word2 = ''
            ___ j __ r..(l..(word1)):
                __ j >= l..(words):
                    r.. False
                __ i >= l..(words[j]):
                    r.. False
                word2 += words[j][i]
            __ word1 != word2:
                r.. False
        r.. True
