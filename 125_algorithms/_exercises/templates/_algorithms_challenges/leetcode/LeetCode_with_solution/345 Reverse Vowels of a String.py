"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""
__author__ = 'Daniel'


class Solution(object):
    ___ reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s = l..(s)
        j = l..(s) - 1
        i = 0
        while i < j:
            __ s[i] __ vowels:
                while s[j] n.. __ vowels: j -= 1
                s[i], s[j] = s[j], s[i]
                j -= 1

            i += 1

        r.. "".join(s)