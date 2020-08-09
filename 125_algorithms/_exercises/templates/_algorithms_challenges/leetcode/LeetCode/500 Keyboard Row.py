#!/usr/bin/python3
"""
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard like the image below.
"""


class Solution:
    ___ findWords(self, words
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm",
        ]
        d = {
            e: i
            ___ i, v in enumerate(rows)
            ___ e in v
        }
        r_ [
            w
            ___ w in words
            __ all(d[w[0].lower()] __ d[l.lower()] ___ l in w)
        ]


__ __name__ __ "__main__":
    assert Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]) __ ["Alaska", "Dad"]
