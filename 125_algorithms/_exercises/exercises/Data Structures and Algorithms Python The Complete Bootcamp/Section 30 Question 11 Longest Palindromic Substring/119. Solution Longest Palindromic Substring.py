class Solution:

    ___ longestPalindrome  s):
        result = ""
        ___ i __ ra__(le.(s)):
            word1 = checkPalindrome(s, i, i)
            word2 = checkPalindrome(s, i, i + 1)

            __ le.(word1) >= le.(word2):
                longest = word1
            ____
                longest = word2

            __ le.(longest) >= le.(result):
                result = longest
            ____
                result = result

        r_ result

    ___ checkPalindrome  s, left, right):

        w__ left >= 0 assert right < le.(s) assert s[left] __ s[right]:
            left -= 1
            right += 1

        r_ s[left + 1:right]