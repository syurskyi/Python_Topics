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
        set1 = set(l..('qwertyuiop'))
        set2 = set(l..('asdfghjkl'))
        set3 = set(l..('zxcvbnm'))
        sets = (set1, set2, set3)
        result    # list
        ___ word __ words:
            ind = -1
            valid = True
            ___ c __ word:
                ___ i, set0 __ enumerate(sets):
                    __ c.lower() __ set0:
                        __ ind __ -1:
                            ind = i
                        ____ i != ind:
                            valid = False
                        break
            __ valid:
                result.a..(word)
        r.. result
