#!/usr/bin/python3
"""
Given two strings A and B of lowercase letters, return true if and only if we
can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""
USED = True


class Solution:
    ___ buddyStrings(self, A: str, B: str) -> bool:
        """
        iterate
        """
        __ len(A) != len(B):
            return False
        __ A == B:
            # find dup
            seen = set()
            for a in A:
                __ a in seen:
                    return True
                seen.add(a)
            else:
                return False

        # Find a pair
        pair = None
        for i in range(len(A)):
            __ A[i] != B[i]:
                __ not pair:
                    pair = (A[i], B[i])
                elif pair == (B[i], A[i]):
                    pair = USED
                else:
                    return False

        __ pair is None or pair is USED:
            return True

        return False
