class Solution:

    ___ longestPalindrome(self, s):
        result  ""
        ___ i __ r..(l..(s)):
            word1  self.checkPalindrome(s, i, i)
            word2  self.checkPalindrome(s, i, i + 1)

            __ l..(word1) > l..(word2):
                longest  word1
            ____:
                longest  word2

            __ l..(longest) > l..(result):
                result  longest
            ____:
                result  result

        r.. result

    ___ checkPalindrome(self, s, left, right):

        w___ left > 0 and right < l..(s) and s[left] __ s[right]:
            left - 1
            right + 1

        r.. s[left + 1:right]