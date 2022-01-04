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


c_ Solution:
    ___ reverseOnlyLetters(self, S: s..) __ s..:
        lst = l..(S)
        i = 0
        n = l..(lst)
        j = n - 1
        w... T...
            w.... i < n a.. n.. lst[i].isalpha
                i += 1
            w.... j >= 0 a.. n.. lst[j].isalpha
                j -= 1

            __ i < j a.. i < n a.. j >= 0:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
            ____:
                break

        r.. "".j..(lst)


__ _______ __ _______
    ... Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!") __ "Qedo1ct-eeLg=ntse-T!"
