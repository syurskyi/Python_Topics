class Solution:
    """
    @param g: the sorted matrix
    @return: the number of Negative Number
    """
    ___ countNumber(self, g
        ans = 0
        __ not g or not g[0]:
            r_ ans

        m, n = le.(g), le.(g[0])

        ___ i in range(m
            left, right = 0, n - 1

            w___ left + 1 < right:
                mid = (left + right) // 2
                __ g[i][mid] < 0:
                    left = mid
                ____
                    right = mid

            __ g[i][left] >= 0:
                continue

            ans += left + 1 __ g[i][right] >= 0 else right + 1

        r_ ans
