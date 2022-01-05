'''
Created on May 10, 2017

@author: MT
'''

c_ Solution(object):
    ___ findWords  words):
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
            valid = T..
            ___ c __ word:
                ___ i, set0 __ e..(sets):
                    __ c.l.. __ set0:
                        __ ind __ -1:
                            ind = i
                        ____ i != ind:
                            valid = F..
                        break
            __ valid:
                result.a..(word)
        r.. result
