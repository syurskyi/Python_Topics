#!/usr/bin/python3
"""
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard like the image below.
"""


class Solution:
    ___ findWords(self, words):
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
            ___ i, v __ enumerate(rows)
            ___ e __ v
        }
        r.. [
            w
            ___ w __ words
            __ a..(d[w[0].lower()] __ d[l.lower()] ___ l __ w)
        ]


__ __name__ __ "__main__":
    ... Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]) __ ["Alaska", "Dad"]
