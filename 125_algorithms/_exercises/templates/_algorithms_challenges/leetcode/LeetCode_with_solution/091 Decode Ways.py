"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
__author__ = 'Danyang'


c_ Solution(o..
    ___ numDecodings  s
        """
        F
        Let F[i] be the number of decode ways for s[:i]
        - 1 2 2 3 1 2 2 3
        1 1 2 ? ?
        F[i] = (F[i-1]) + optional(F[i-2]))

        notice the special handling for "0

        :param s: a string
        :return: an integer
        """
        __ s.startswith("0"
            r.. 0

        n = l..(s)
        __ n.. s:
            r.. 0
        F = [0 ___ _ __ x..(n+1)]
        F[0] = 1
        F[1] = 1

        ___ i __ x..(2, n+1
            __ s[i-1] != "0":
                F[i] = F[i-1]
                __ 10 <= i..(s[i-2]+s[i-1]) < 27:
                    F[i] += F[i-2]
            ____:  # 0 is special
                __ s[i-2] __ ("1", "2"
                    F[i] = F[i-2]
                ____:
                    r.. 0

        r.. F[-1]


__ _______ __ _______
    ... Solution().numDecodings("10") __ 1
    ... Solution().numDecodings("27") __ 1
    ... Solution().numDecodings("12") __ 2
    ... Solution().numDecodings("0") __ 0