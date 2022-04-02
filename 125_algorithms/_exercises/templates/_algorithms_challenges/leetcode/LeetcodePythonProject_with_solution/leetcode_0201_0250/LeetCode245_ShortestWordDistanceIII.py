'''
Created on May 14, 2018

@author: tongq
'''
c_ Solution(o..
    ___ shortestWordDistance  words, word1, word2
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = f__('inf')
        ___ i, word __ e..(words
            __ word __ [word1, word2]:
                target = word2 __ word __ word1 ____ word1
                j = i+1
                w.... j < l..(words
                    __ words[j] __ target:
                        res = m..(res, j-i)
                    j += 1
        r.. res
