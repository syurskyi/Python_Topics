#!/usr/bin/python3
"""
Given a non-empty string s, you may delete at most one character. Judge whether
you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the
string is 50000.
"""


c_ Solution:
    ___ validPalindrome(self, s: s..) -> bool:
        """
        Brute force, delete and check. O(n^2)

        Start from start and end, then check equal. If not match, skip either
        side (i.e. delete a character), then check palindrome
        """
        n = l..(s)
        i = 0
        j = n - 1
        w.... i < j:
            __ s[i] __ s[j]:
                i += 1
                j -= 1
            ____:
                # error, for -1, start > end. Indexing is like range
                # return s[i:j] == s[i:j:-1] or s[i+1:j+1] == s[i+1:j+1:-1]
                r.. is_palindrome(s[i:j]) o. is_palindrome(s[i+1:j+1])

        r.. T..

    ___ is_palindrome(self, s):
        r.. s __ s[::-1]


__ __name__ __ "__main__":
    ... Solution().validPalindrome("aba") __ T..
    ... Solution().validPalindrome("abca") __ T..
