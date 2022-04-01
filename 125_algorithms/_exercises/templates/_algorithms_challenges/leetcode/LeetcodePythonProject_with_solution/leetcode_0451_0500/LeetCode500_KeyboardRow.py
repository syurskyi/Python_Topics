'''
Created on May 10, 2017

@author: MT
'''

c_ Solution(o..):
    ___ findWords  words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = s..(l..('qwertyuiop'))
        set2 = s..(l..('asdfghjkl'))
        set3 = s..(l..('zxcvbnm'))
        sets = (set1, set2, set3)
        result    # list
        ___ word __ words:
            ind = -1
            valid = T..
            ___ c __ word:
                ___ i, set0 __ e..(sets):
                    __ c.l.. __ set0:
                        __ ind __ -1:
                            ind = i
                        ____ i != ind:
                            valid = F..
                        _____
            __ valid:
                result.a..(word)
        r.. result
