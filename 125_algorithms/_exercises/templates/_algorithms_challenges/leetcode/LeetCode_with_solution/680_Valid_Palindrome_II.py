c_ Solution o..
    # def validPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     def is_pali_range(i, j):
    #         return all(s[k] == s[j - k + i] for k in range(i, j))

    #     for i in xrange(len(s) / 2):
    #         if s[i] != s[~i]:
    #             j = len(s) - 1 - i
    #             return is_pali_range(i + 1, j) or is_pali_range(i, j - 1)
    #     return True

    # Actually we can make this solution more general
    ___ validPalindrome  s
        r_ validPalindromeHelper(s, 0, l.. s) - 1, 1)

    ___ validPalindromeHelper  s, left, right, budget
        # Note that budget can be more than 1
        w.. left < l.. s) a.. right >= 0 a.. left <= right a.. s[left] __ s[right]:
            left += 1
            right -= 1
        __ left >= l.. s) or right < 0 or left >= right:
            r_ T..
        __ budget __ 0:
            r_ F..
        budget -= 1
        r_ validPalindromeHelper(s, left + 1, right, budget) or validPalindromeHelper(s, left, right - 1, budget)
