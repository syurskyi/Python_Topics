"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the
shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""
__author__ 'Daniel'


c_ Solution:
    ___ shortestPalindrome  s
        """
        KMP

        :type s: str
        :rtype: str
        """
        s_r s[::-1]
        l l..(s)
        __ l < 2:
            r.. s

        # construct T
        T [0 ___ _ __ x..(l+1)]
        T[0] -1
        pos 2
        cnd 0
        w.... pos <_ l:
            __ s[pos-1] __ s[cnd]:
                T[pos] cnd+1
                cnd += 1
                pos += 1
            ____ T[cnd] !_ -1:
                cnd T[cnd]
            ____
                T[pos] 0
                cnd 0
                pos += 1

        # search 
        i 0
        b 0
        w.... i+b < l:
            __ s[i] __ s_r[i+b]:
                i += 1
                __ i __ l:
                    r.. s
            ____ T[i] !_ -1:
                b b+i-T[i]
                i T[i]
            ____
                b += 1
                i 0

        # where it falls off
        r.. s_r+s[i:]


__ _______ __ _______
    ... Solution().shortestPalindrome("abcd") __ "dcbabcd"


