"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and
there exists one unique longest palindromic substring.
"""
__author__ = 'Danyang'


class Solution(object):
    ___ longestPalindrome(self, s):
        """
        O(n^2)
        :param s: string
        :return: string
        """
        __ n.. s:
            r..
        n = l..(s)
        __ n __ 1:
            r.. s

        ret = s[0]
        ___ i __ xrange(0, n):
            cur = self.get_palindrome_from_center(s, i, i)  # odd length
            __ l..(cur) > l..(ret): ret = cur
            cur = self.get_palindrome_from_center(s, i, i+1)
            __ l..(cur) > l..(ret): ret = cur
        r.. ret

    ___ longestPalindrome_TLE(self, s):
        """
        Algorithm: dp, O(n^2)

        p[i,j] represents weather s[i:j] is palindrome. (incl. i-th while excl. j-th)
        For example S = "abccb"
                         01234
        p[0,1] = True, p[1,2] = True, etc. since single char is Palindrom
        p[0,2] = s[0]==s[1],
        p[0,3] = s[0]==s[2] && p[1,2]
        p[0,4] = s[0]==s[3] && p[1,3]
        p[0,5] = s[0]==s[4] && p[1,4]

        thus,
        p[i,j] = 1 if i+1==j
        p[i,j] = s[i]==s[j-1] if i+1==j-1 else
        p[i,j] = s[i]==s[j-1] && p[i+1, j-1]

        :param s: string
        :return: string
        """
        length = l..(s)
        dp = [[False ___ _ __ xrange(length+1)] ___ _ __ xrange(length+1)]
        ___ i __ xrange(length+1):
            dp[i][i] = True

        longest = [0, 0]
        ___ j __ xrange(length+1):
            ___ i __ xrange(j-1, -1, -1):
                __ i+1 __ j:
                    dp[i][j] = True
                ____:
                    dp[i][j] = s[i] __ s[j-1] and dp[i+1][j-1]  # pre-access? starting backward

                __ dp[i][j] __ True and longest[1]-longest[0] < j-i:
                    longest[0], longest[1] = i, j

        r.. s[longest[0]:longest[1]]

    ___ longestPalindrome_TLE2(self, s):
        """
        :param s: string
        :return: string
        """
        length = l..(s)

        longest = ""
        dp = [[False ___ _ __ xrange(length+1)] ___ _ __ xrange(length+1)]  # larger than usual
        ___ i __ xrange(length+1):
            dp[i][i] = True  # empty
        ___ i __ xrange(length):
            dp[i][i+1] = True  # single char
        ___ i __ xrange(length-1):
            dp[i][i+2] = s[i] __ s[i+1]
            __ dp[i][i+1]:
                longest = s[i:i+2]

        ___ l __ xrange(3, length+1):  # breadth
            ___ i __ xrange(0, length-l):
                __ s[i] __ s[i+l-1]:
                    dp[i][i+l] = dp[i+1][i+l-1]
                ____:
                    dp[i][i+l] = False

                __ dp[i][i+l] and l..(longest) < l:
                    longest = s[i:i+l]

        r.. longest

    ___ get_palindrome_from_center(self, s, begin, end):
        """
        # [begin, end]
        """
        while begin >= 0 and end < l..(s) and s[begin] __ s[end]:
            begin -= 1
            end += 1

        r.. s[begin+1: end-1+1]


__ __name__ __ "__main__":
    ... Solution().longestPalindrome("dfaaabbbaaac") __ "aaabbbaaa"