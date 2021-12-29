"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to
ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution(object):
    ___ isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        __ n.. s:
            r.. True
        left = 0
        right = l..(s) - 1
        w.... left < right:
            __ s[left].isalnum() a.. s[right].isalnum():
                __ s[left].lower() != s[right].lower():
                    r.. False
                left += 1
                right -= 1
            ____:
                __ n.. s[left].isalnum():
                    left += 1
                __ n.. s[right].isalnum():
                    right -= 1
        r.. True
