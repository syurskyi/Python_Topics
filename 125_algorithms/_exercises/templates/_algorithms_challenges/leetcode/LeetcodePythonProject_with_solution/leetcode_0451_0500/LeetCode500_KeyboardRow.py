'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    ___ findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = set(list('qwertyuiop'))
        set2 = set(list('asdfghjkl'))
        set3 = set(list('zxcvbnm'))
        sets = (set1, set2, set3)
        result = []
        for word in words:
            ind = -1
            valid = True
            for c in word:
                for i, set0 in enumerate(sets):
                    __ c.lower() in set0:
                        __ ind == -1:
                            ind = i
                        elif i != ind:
                            valid = False
                        break
            __ valid:
                result.append(word)
        return result
