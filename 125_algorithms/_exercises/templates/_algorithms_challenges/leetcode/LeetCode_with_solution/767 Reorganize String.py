#!/usr/bin/python3
"""
Given a string S, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty
string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
____ c.. _______ d..


c_ Solution:
    ___ reorganizeString  S: s..) __ s..
        """
        piles by max char and circular append
        """
        counter d..(i..)
        ___ c __ S:
            counter[c] += 1

        lst [
            (-n, n, c)
            ___ c, n __ counter.i..
        ]
        lst.s..()
        piles    # list
        _, n, c lst[0]
        ___ i __ r..(n
            piles.a..([c])

        cnt 0
        ___ _, n, c __ lst 1|
            ___ _ __ r..(n
                piles[cnt].a..(c)
                cnt (cnt + 1) % l..(piles)

        __ l..(piles) > 1 a.. l..(piles -2 __ 1:
            r.. ""

        r.. "".j..(
            m.. l.... x: "".j..(x), piles)
        )


__ _______ __ _______
    ... Solution().reorganizeString("vvvlo") __ "vlvov"
    ... Solution().reorganizeString("aab") __ "aba"
    ... Solution().reorganizeString("aaab") __ ""
