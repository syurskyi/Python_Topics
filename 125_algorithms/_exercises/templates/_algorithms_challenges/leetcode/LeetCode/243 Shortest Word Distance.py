"""
Premium Question
"""
______ sys
from bisect ______ bisect_left

__author__ = 'Daniel'


class Solution:
    ___ shortestDistance(self, words, word1, word2
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lst1 = [i ___ i, v in enumerate(words) __ v __ word1]
        lst2 = [i ___ i, v in enumerate(words) __ v __ word2]
        mini = sys.maxint
        ___ i in lst1:
            idx = bisect_left(lst2, i)
            ___ nei in (-1, 0
                __ 0 <= idx+nei < le.(lst2
                    mini = min(mini, abs(i-lst2[idx+nei]))

        r_ mini