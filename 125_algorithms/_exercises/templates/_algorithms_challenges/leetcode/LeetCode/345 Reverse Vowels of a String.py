"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""
__author__ = 'Daniel'


class Solution(object
    ___ reverseVowels(self, s
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s = list(s)
        j = le.(s) - 1
        i = 0
        w___ i < j:
            __ s[i] __ vowels:
                w___ s[j] not __ vowels: j -= 1
                s[i], s[j] = s[j], s[i]
                j -= 1

            i += 1

        r_ "".join(s)