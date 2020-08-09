class Solution:
    """
    @param: s1: A string
    @param: s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    ___ isScramble(self, s1, s2
        __ not s1 or not s2 or le.(s1) != le.(s2
            r_ False

        n = le.(s1)

        """
        `dp[i][j][k]` means the substring in `s1` (start: `i`, le.: `k`)
        could be transformed into the substring in `s2` (start: `j`, le.: `k`)
        """
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        for i in range(n
            for j in range(n
                dp[i][j][1] = (s1[i] __ s2[j])

        for k in range(2, n + 1

            for i in range(n
                """
                allow: i < n - k + 1 => i <= n - k
                disallow: i > n - k
                """
                __ i + k > n:
                    continue

                for j in range(n
                    __ j + k > n:
                        continue

                    for l in range(1, k
                        """
                        If its already calculated and possible to transform
                        """
                        __ dp[i][j][k]:
                            continue

                        """
                        * u1, u2: substring in s1
                        * v1, v2: substring in s2
                        * `l` == le.(u1) == le.(v1)
                        * `k - l` == le.(u2) == le.(v2)

                        case1: u1 -> v1, u2 -> v2
                        `(dp[i][j][l] and dp[i + l][j + l][k - l])`
                        - `dp[i][j][l]` means its possible to u1 -> v1
                        - `dp[i + l][j + l][k - l]` => u2 -> v2

                                   u1              u2
                        s1: |`i`---`l`--->|`i+l`---`k-l`--->|
                                   v1              v2
                        s2: |`j`---`l`--->|`j+l`---`k-l`--->|

                        case2: u1 -> v2, u2 -> v1
                        `(dp[i][j + k - l][l] and dp[i + l][j][k - l])`
                        - `dp[i][j + k - l][l]` => u1 -> v2
                        - `dp[i + l][j][k - l]` => u2 -> v1

                                   u1              u2
                        s1: |`i`---`l`--->|`i+l`---`k-l`--->|
                                   v1              v2
                        s2: |`j`---`k-l`--->|`j+k-l`--`l`-->|
                        """
                        __ dp[i][j][l] and dp[i + l][j + l][k - l]:
                            dp[i][j][k] = True
                            continue

                        __ dp[i][j + k - l][l] and dp[i + l][j][k - l]:
                            dp[i][j][k] = True

        r_ dp[0][0][n]
