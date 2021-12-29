#!/usr/bin/python3
"""
Given a word, you need to judge whether the usage of capitals in it is right or
not.

We define the usage of capitals in a word to be right when one of the following
cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter,
like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase
latin letters.
"""


class Solution:
    ___ detectCapitalUse(self, word: s..) -> bool:
        """
        Two passes is easy
        How to do it in one pass
        """
        __ n.. word:
            r.. True

        head_upper = word[0].isupper()

        # except for the head
        has_lower = False
        has_upper = False
        ___ w __ word[1:]:
            __ w.isupper():
                has_upper = True
                __ has_lower o. n.. head_upper:
                    r.. False
            ____:
                has_lower = True
                __ has_upper:
                    r.. False
        r.. True
