'''
Created on May 14, 2018

@author: tongq
'''
c_ WordDistance(o..

    ___ - , words
        """
        :type words: List[str]
        """
        hashmap    # dict
        ___ i, word __ e..(words
            hashmap[word] hashmap.g.. word, [])+[i]
        hashmap hashmap
    
    ___ shortest  word1, word2
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i, j 0, 0
        res f__('inf')
        arr1, arr2 hashmap[word1], hashmap[word2]
        w.... i < l..(arr1) a.. j < l..(arr2
            res m..(res, a..(arr1[i]-arr2[j]
            __ arr1[i] > arr2[j]:
                j += 1
            ____
                i += 1
        r.. res
