"""
Your ValidWordAbbr object will be instantiated and called as such:
vwa = ValidWordAbbr(dictionary)
vwa.isUnique("word")
vwa.isUnique("anotherWord")

Testing:
>>> s = ValidWordAbbr(['deer', 'door', 'cake', 'card'])
>>> all((
...     s.isUnique('dear') is False,
...     s.isUnique('cart') is True,
...     s.isUnique('cane') is False,
...     s.isUnique('make') is True,
... ))
True
"""


c_ ValidWordAbbr:
    ___ - , dictionary
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        abbrs    # dict

        ___ word __ dictionary:
            abbr abbreviation(word)
            abbrs[abbr] word

    ___ isUnique  word
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr abbreviation(word)
        r.. abbr n.. __ abbrs

    ___ abbreviation  word
        __ l.. ? < 3:
            r.. word

        cnt l.. ? - 2
        r.. '{}{}{}'.f..(
            word[0],
            s..(cnt),
            word[-1]
        )
