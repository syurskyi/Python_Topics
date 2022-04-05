c_ Solution:
    ___ PalindromicRanges  left, right
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        __ left > right:
            r.. 0
        __ left __ right:
            r.. 1

        dp = [0] * (right - left + 2)  # n + 1, n = right - left + 1
        # dp[0] = 0

        ___ num __ r..(left, right + 1
            __ is_palindrome(num
                dp[num - left + 1] = dp[num - left] + 1
            ____
                dp[num - left + 1] = dp[num - left]

        ans = 0

        ___ i __ r..(1, right - left + 2
            ___ j __ r..(i
                __ ((dp[i] - dp[j]) & 1 __ 0
                    ans += 1

        r.. ans

    ___ is_palindrome  num
        __ num // 10 __ 0:
            r.. T..

        s = s..(num)
        left, right = 0, l..(s) - 1

        w.... left < right:
            __ s[left] != s[right]:
                r.. F..

            left += 1
            right -_ 1

        r.. T..
