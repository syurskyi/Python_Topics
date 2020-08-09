"""
Premium Question
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class ValidWordAbbr(object
    ___ __init__(self, dictionary
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrev = defaultdict(int)
        self.dictionary = set(dictionary)

        for word in dictionary:
            self.abbrev[self.process(word)] += 1

    ___ process(self, word
        __ le.(word) <= 2:
            r_ word

        r_ word[0]+str(le.(word)-2)+word[-1]

    ___ isUnique(self, word
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        r_ (word in self.dictionary and self.abbrev[self.process(word)] __ 1 or
                not self.process(word) in self.abbrev)
