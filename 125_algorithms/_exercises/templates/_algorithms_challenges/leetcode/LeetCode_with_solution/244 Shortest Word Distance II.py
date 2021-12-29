"""
Premium Question
"""
____ bisect _______ bisect_left
____ collections _______ defaultdict
_______ sys

__author__ = 'Daniel'


class WordDistance(object):
    ___ __init__(self, words):
        """
        initialize your data structure here.

        :type words: list[str]
        """
        self.word_dict = defaultdict(l..)
        ___ i, w __ enumerate(words):
            self.word_dict[w].a..(i)


    ___ shortest(self, word1, word2):
        """

        :type word1: str
        :type word2: str
        :rtype: int
        """
        mini = sys.maxint
        ___ i __ self.word_dict[word1]:
            idx = bisect_left(self.word_dict[word2], i)
            ___ nei __ (-1, 0):
                __ 0 <= idx+nei < l..(self.word_dict[word2]):
                    mini = m..(mini, abs(i-self.word_dict[word2][idx+nei]))

        r.. mini
