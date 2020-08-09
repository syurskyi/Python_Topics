"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
__author__ = 'Danyang'


class Solution(object
    ___ isPalindrome(self, s
        """

        :param s: a string
        :return: a boolean
        """
        s = s.lower()
        # ______ re  # not supported
        # s = re.sub('[^a-zA-Z0-9]', '', s)  # not supported
        s = ''.join(e ___ e in s __ e.isalnum())
        __ not s:
            r_ True

        r_ s __ s[::-1]