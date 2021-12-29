class Solution:
    """
    @param g: the sorted matrix
    @return: the number of Negative Number
    """
    ___ countNumber(self, g):
        ans = 0
        __ not g or not g[0]:
            return ans

        m, n = len(g), len(g[0])

        for i in range(m):
            left, right = 0, n - 1

            while left + 1 < right:
                mid = (left + right) // 2
                __ g[i][mid] < 0:
                    left = mid
                else:
                    right = mid

            __ g[i][left] >= 0:
                continue

            ans += left + 1 __ g[i][right] >= 0 else right + 1

        return ans
