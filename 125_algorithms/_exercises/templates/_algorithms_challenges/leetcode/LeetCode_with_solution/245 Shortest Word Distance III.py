"""
Premium Question
"""
_______ ___
____ bisect _______ bisect_left

__author__ = 'Daniel'


c_ Solution(o..
    ___ shortestWordDistance  words, word1, word2
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos_lst1 = [pos ___ pos, v __ e..(words) __ v __ word1]
        pos_lst2 = [pos ___ pos, v __ e..(words) __ v __ word2]
        mini = ___.maxint
        ___ pos __ pos_lst1:
            idx = bisect_left(pos_lst2, pos)
            ___ nei __ (-1, 0
                __ 0 <= idx+nei < l..(pos_lst2) a.. pos != pos_lst2[idx+nei]:
                    mini = m..(mini, abs(pos-pos_lst2[idx+nei]

        r.. mini
