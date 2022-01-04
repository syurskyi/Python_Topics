"""
Premium Question
"""
____ bisect _______ bisect_left
____ c.. _______ defaultdict
_______ sys

__author__ = 'Daniel'


c_ WordDistance(object):
    ___ - , words):
        """
        initialize your data structure here.

        :type words: list[str]
        """
        word_dict = defaultdict(l..)
        ___ i, w __ e..(words):
            word_dict[w].a..(i)


    ___ shortest(self, word1, word2):
        """

        :type word1: str
        :type word2: str
        :rtype: int
        """
        mini = sys.maxint
        ___ i __ word_dict[word1]:
            idx = bisect_left(word_dict[word2], i)
            ___ nei __ (-1, 0):
                __ 0 <= idx+nei < l..(word_dict[word2]):
                    mini = m..(mini, abs(i-word_dict[word2][idx+nei]))

        r.. mini
