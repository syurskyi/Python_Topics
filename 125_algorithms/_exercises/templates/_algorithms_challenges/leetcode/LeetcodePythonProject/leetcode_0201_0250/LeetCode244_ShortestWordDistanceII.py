'''
Created on May 14, 2018

@author: tongq
'''
class WordDistance(object

    ___ __init__(self, words
        """
        :type words: List[str]
        """
        hashmap = {}
        ___ i, word in enumerate(words
            hashmap[word] = hashmap.get(word, [])+[i]
        self.hashmap = hashmap
    
    ___ shortest(self, word1, word2
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i, j = 0, 0
        res = float('inf')
        arr1, arr2 = self.hashmap[word1], self.hashmap[word2]
        w___ i < le.(arr1) and j < le.(arr2
            res = min(res, abs(arr1[i]-arr2[j]))
            __ arr1[i] > arr2[j]:
                j += 1
            ____
                i += 1
        r_ res
