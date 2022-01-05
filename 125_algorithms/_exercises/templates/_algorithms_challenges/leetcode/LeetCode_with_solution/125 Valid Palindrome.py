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


c_ Solution(object):
    ___ isPalindrome  s):
        """

        :param s: a string
        :return: a boolean
        """
        s = s.l..
        # import re  # not supported
        # s = re.sub('[^a-zA-Z0-9]', '', s)  # not supported
        s = ''.j..(e ___ e __ s __ e.isalnum())
        __ n.. s:
            r.. T..

        r.. s __ s[::-1]