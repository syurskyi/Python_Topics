#!/usr/bin/python3
"""
We are given two sentences A and B.  (A sentence is a string of space separated
words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does
not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""
____ t___ _______ L..
____ c.. _______ C..


c_ Solution:
    ___ uncommonFromSentences  A: s.., B: s..) __ L.. s..
        """
        need counter, only need to appear once
        """
        c C..(A.s.. + C..(B.s..
        ret [
            k
            ___ k, v __ c.i..
            __ v __ 1
        ]
        r.. ret

    ___ uncommonFromSentences_complext  A: s.., B: s..) __ L.. s..
        """
        need counter
        """
        c_A, c_B C..(A.s.., C..(B.s..
        ret    # list
        ___ k, v __ c_A.i..
            __ v __ 1 a.. k n.. __ c_B:
                ret.a..(k)

        ___ k, v __ c_B.i..
            __ v __ 1 a.. k n.. __ c_A:
                ret.a..(k)

        r.. ret

    ___ uncommonFromSentences_error  A: s.., B: s..) __ L.. s..
        """
        set difference
        """
        s_A, s_B s..(A.s.., s..(B.s..
        r.. l..(
            (s_A - s_B) | (s_B - s_A)
        )
