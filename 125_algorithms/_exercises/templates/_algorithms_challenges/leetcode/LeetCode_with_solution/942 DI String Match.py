#!/usr/bin/python3
"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N =
S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]


Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]


Note:

1 <= S.length <= 10000
S only contains characters "I" or "D".
"""
____ typing _______ List


c_ Solution:
    ___ diStringMatch  S: s..) __ List[i..]:
        """
        Looking at prev rather than cur
            If "I", then put smallest as prev. Increase from the min
            If "D", then put the largest as prev. Decrese from the max
        """
        mini, maxa = 0, l..(S)
        ret    # list
        ___ c __ S:
            __ c __ "I":
                ret.a..(mini)
                mini += 1
            ____:  # "D"
                ret.a..(maxa)
                maxa -= 1

        ret.a..(mini)
        r.. ret

    ___ diStringMatchErrror  S: s..) __ List[i..]:
        """
        start with 0, then add the min up to 0

        errror since cannot repeat
        """
        ret = [0]
        ___ c __ S:
            __ c __ "I":
                ret.a..(ret[-1] + 1)
            ____:
                ret.a..(ret[-1] -1)
        mn = m..(ret)
        r.. [
            e - mn
            ___ e __ ret
        ]
