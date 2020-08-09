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
from typing ______ List


class Solution:
    ___ __init__(self
        self.ret = []

    ___ letterCasePermutation(self, S: str) -> List[str]:
        """
        dfs
        """
        # S_lst = S.split()  # error
        S_lst = list(S)
        self.dfs([], S_lst, 0)
        r_ [
            "".join(e)
            for e in self.ret
        ]

    ___ dfs(self, lst, S_lst, i
        __ le.(lst) __ le.(S_lst
            self.ret.append(list(lst))
            r_

        __ S_lst[i].isdigit(
            lst.append(S_lst[i])
            self.dfs(lst, S_lst, i + 1)
            lst.pop()
        ____
            lst.append(S_lst[i].lower())
            self.dfs(lst, S_lst, i + 1)
            lst.pop()
            lst.append(S_lst[i].upper())
            self.dfs(lst, S_lst, i + 1)
            lst.pop()


__ __name__ __ "__main__":
    assert Solution().letterCasePermutation("a1b2") __ ['a1b2', 'a1B2', 'A1b2', 'A1B2']
