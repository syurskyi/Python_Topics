#!/usr/bin/python3
"""
Given a string S, we can transform every letter individually to be lowercase or
uppercase to create another string.  Return a list of all possible strings we
could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
____ typing _______ List


c_ Solution:
    ___ - ):
        ret    # list

    ___ letterCasePermutation  S: s..) __ List[s..]:
        """
        dfs
        """
        # S_lst = S.split()  # error
        S_lst = l..(S)
        dfs([], S_lst, 0)
        r.. [
            "".j..(e)
            ___ e __ ret
        ]

    ___ dfs  lst, S_lst, i):
        __ l..(lst) __ l..(S_lst):
            ret.a..(l..(lst))
            r..

        __ S_lst[i].i..
            lst.a..(S_lst[i])
            dfs(lst, S_lst, i + 1)
            lst.pop()
        ____:
            lst.a..(S_lst[i].lower())
            dfs(lst, S_lst, i + 1)
            lst.pop()
            lst.a..(S_lst[i].upper())
            dfs(lst, S_lst, i + 1)
            lst.pop()


__ _______ __ _______
    ... Solution().letterCasePermutation("a1b2") __ ['a1b2', 'a1B2', 'A1b2', 'A1B2']
