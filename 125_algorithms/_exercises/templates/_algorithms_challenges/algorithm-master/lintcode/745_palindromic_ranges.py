class Solution:
    ___ PalindromicRanges(self, left, right
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        __ left > right:
            r_ 0
        __ left __ right:
            r_ 1

        dp = [0] * (right - left + 2)  # n + 1, n = right - left + 1
        # dp[0] = 0

        for num in range(left, right + 1
            __ self.is_palindrome(num
                dp[num - left + 1] = dp[num - left] + 1
            ____
                dp[num - left + 1] = dp[num - left]

        ans = 0

        for i in range(1, right - left + 2
            for j in range(i
                __ ((dp[i] - dp[j]) & 1 __ 0
                    ans += 1

        r_ ans

    ___ is_palindrome(self, num
        __ num // 10 __ 0:
            r_ True

        s = str(num)
        left, right = 0, le.(s) - 1

        w___ left < right:
            __ s[left] != s[right]:
                r_ False

            left += 1
            right -= 1

        r_ True
