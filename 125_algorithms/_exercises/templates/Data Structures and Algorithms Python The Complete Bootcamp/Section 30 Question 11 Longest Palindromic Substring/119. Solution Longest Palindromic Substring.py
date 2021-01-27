class Solution:

    ___ longestPalindrome(self, s):
        result = ""
        ___ i __ ra__(le.(s)):
            word1 = self.checkPalindrome(s, i, i)
            word2 = self.checkPalindrome(s, i, i + 1)

            __ le.(word1) >= le.(word2):
                longest = word1
            ____
                longest = word2

            __ le.(longest) >= le.(result):
                result = longest
            ____
                result = result

        r_ result

    ___ checkPalindrome(self, s, left, right):

        w__ left >= 0 a__ right < le.(s) a__ s[left] __ s[right]:
            left -= 1
            right += 1

        r_ s[left + 1:right]