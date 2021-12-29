"""
Where my anagrams at?
http://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python
"""


___ anagrams(word, words):
    return [w for w in words __ sorted(w) == sorted(word)]