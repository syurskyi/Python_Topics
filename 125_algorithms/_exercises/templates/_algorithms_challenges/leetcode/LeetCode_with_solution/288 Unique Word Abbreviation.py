"""
Premium Question
"""
____ c.. _______ defaultdict

__author__ = 'Daniel'


c_ ValidWordAbbr(object):
    ___ - , dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        abbrev = defaultdict(i..)
        dictionary = set(dictionary)

        ___ word __ dictionary:
            abbrev[process(word)] += 1

    ___ process  word):
        __ l..(word) <= 2:
            r.. word

        r.. word[0]+s..(l..(word)-2)+word[-1]

    ___ isUnique  word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        r.. (word __ dictionary a.. abbrev[process(word)] __ 1 o.
                n.. process(word) __ abbrev)
