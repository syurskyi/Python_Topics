"""
Premium Question
"""
______ sys
from bisect ______ bisect_left

__author__ = 'Daniel'


class Solution(object
    ___ shortestWordDistance(self, words, word1, word2
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos_lst1 = [pos for pos, v in enumerate(words) __ v __ word1]
        pos_lst2 = [pos for pos, v in enumerate(words) __ v __ word2]
        mini = sys.maxint
        for pos in pos_lst1:
            idx = bisect_left(pos_lst2, pos)
            for nei in (-1, 0
                __ 0 <= idx+nei < le.(pos_lst2) and pos != pos_lst2[idx+nei]:
                    mini = min(mini, abs(pos-pos_lst2[idx+nei]))

        r_ mini
