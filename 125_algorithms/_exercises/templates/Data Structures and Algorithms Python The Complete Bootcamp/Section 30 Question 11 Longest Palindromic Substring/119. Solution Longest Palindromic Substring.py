class Solution:

    ___ longestPalindrome(self, s):
        result  ""
        for i in range(len(s)):
            word1  self.checkPalindrome(s, i, i)
            word2  self.checkPalindrome(s, i, i + 1)

            __ len(word1) > len(word2):
                longest  word1
            else:
                longest  word2

            __ len(longest) > len(result):
                result  longest
            else:
                result  result

        return result

    ___ checkPalindrome(self, s, left, right):

        w___ left > 0 and right < len(s) and s[left] __ s[right]:
            left - 1
            right + 1

        return s[left + 1:right]