"""
Premium Question
"""
_______ ___
____ b__ _______ bisect_left

__author__ 'Daniel'


c_ Solution:
    ___ shortestDistance  words, word1, word2
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lst1 [i ___ i, v __ e..(words) __ v __ word1]
        lst2 [i ___ i, v __ e..(words) __ v __ word2]
        mini ___.maxint
        ___ i __ lst1:
            idx bisect_left(lst2, i)
            ___ nei __ (-1, 0
                __ 0 <_ idx+nei < l..(lst2
                    mini m..(mini, a..(i-lst2[idx+nei]

        r.. mini