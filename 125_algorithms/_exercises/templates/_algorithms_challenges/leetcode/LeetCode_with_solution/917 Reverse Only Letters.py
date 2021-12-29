#!/usr/bin/python3
"""
Given a string S, return the "reversed" string where all characters that are not
a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""


class Solution:
    ___ reverseOnlyLetters(self, S: str) -> str:
        lst = l..(S)
        i = 0
        n = l..(lst)
        j = n - 1
        while True:
            while i < n and n.. lst[i].isalpha():
                i += 1
            while j >= 0 and n.. lst[j].isalpha():
                j -= 1

            __ i < j and i < n and j >= 0:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
            ____:
                break

        r.. "".join(lst)


__ __name__ __ "__main__":
    ... Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!") __ "Qedo1ct-eeLg=ntse-T!"
