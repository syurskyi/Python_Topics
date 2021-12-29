"""
Premium Question
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


class ValidWordAbbr(object):
    ___ __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrev = defaultdict(int)
        self.dictionary = set(dictionary)

        ___ word __ dictionary:
            self.abbrev[self.process(word)] += 1

    ___ process(self, word):
        __ l..(word) <= 2:
            r.. word

        r.. word[0]+s..(l..(word)-2)+word[-1]

    ___ isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        r.. (word __ self.dictionary a.. self.abbrev[self.process(word)] __ 1 o.
                n.. self.process(word) __ self.abbrev)
