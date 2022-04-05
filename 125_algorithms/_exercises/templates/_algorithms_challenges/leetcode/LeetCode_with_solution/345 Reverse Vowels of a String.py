"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""
__author__ = 'Daniel'


c_ Solution(o..
    ___ reverseVowels  s
        """
        :type s: str
        :rtype: str
        """
        vowels = s..( 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' )
        s = l..(s)
        j = l..(s) - 1
        i = 0
        w.... i < j:
            __ s[i] __ vowels:
                w.... s[j] n.. __ vowels: j -_ 1
                s[i], s[j] = s[j], s[i]
                j -_ 1

            i += 1

        r.. "".j..(s)