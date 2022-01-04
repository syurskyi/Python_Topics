#!/usr/bin/python3
"""
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard like the image below.
"""


c_ Solution:
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
            ___ i, v __ e..(rows)
            ___ e __ v
        }
        r.. [
            w
            ___ w __ words
            __ a..(d[w[0].l..] __ d[l.l..] ___ l __ w)
        ]


__ _______ __ _______
    ... Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]) __ ["Alaska", "Dad"]
