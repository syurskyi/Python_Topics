"""
Premium Question
"""
from bisect ______ bisect_left
from collections ______ defaultdict
______ sys

__author__ = 'Daniel'


class WordDistance(object
    ___ __init__(self, words
        """
        initialize your data structure here.

        :type words: list[str]
        """
        self.word_dict = defaultdict(list)
        ___ i, w in enumerate(words
            self.word_dict[w].append(i)


    ___ shortest(self, word1, word2
        """

        :type word1: str
        :type word2: str
        :rtype: int
        """
        mini = sys.maxint
        ___ i in self.word_dict[word1]:
            idx = bisect_left(self.word_dict[word2], i)
            ___ nei in (-1, 0
                __ 0 <= idx+nei < le.(self.word_dict[word2]
                    mini = min(mini, abs(i-self.word_dict[word2][idx+nei]))

        r_ mini
