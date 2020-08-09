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


class ValidWordAbbr:
    ___ __init__(self, dictionary
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrs = {}

        for word in dictionary:
            abbr = self.abbreviation(word)
            self.abbrs[abbr] = word

    ___ isUnique(self, word
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.abbreviation(word)
        r_ abbr not in self.abbrs

    ___ abbreviation(self, word
        __ le.(word) < 3:
            r_ word

        cnt = le.(word) - 2
        r_ '{}{}{}'.format(
            word[0],
            str(cnt),
            word[-1]
        )
