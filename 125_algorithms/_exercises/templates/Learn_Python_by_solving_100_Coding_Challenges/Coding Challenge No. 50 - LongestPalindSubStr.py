# Longest Palindromic Substring
# Question: Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
# Solutions:


c_ Solution:
    # @param {string} s
    # @return {string}

    ___ longestPalindrome(, s):
        l _ le.(s)
        __ l <_ 2:
            __ (s[0] !_ s[l-1]):
                r_ ''
            ____
                r_ s
        result _ ''
        ___ i __ ra..(0,l):
            palindrome _ SearchPalindrome(s, i, i)
            __ le.(palindrome) > le.(result):
                result _ palindrome
            palindrome _ SearchPalindrome(s, i, i+1)
            __ le.(palindrome) > le.(result):
                result _ palindrome
        r_ result

    ___ SearchPalindrome(, string, start, end):
        w___(start>_0 an. end < le.(string) an. string[start]__string[end]):
            start -_ 1
            end +_ 1
        r_ string[start+1:end]


Solution().longestPalindrome("bananas")