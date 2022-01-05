c_ Solution:
    """
    @param g: the sorted matrix
    @return: the number of Negative Number
    """
    ___ countNumber  g):
        ans = 0
        __ n.. g o. n.. g[0]:
            r.. ans

        m, n = l..(g), l..(g[0])

        ___ i __ r..(m):
            left, right = 0, n - 1

            w.... left + 1 < right:
                mid = (left + right) // 2
                __ g[i][mid] < 0:
                    left = mid
                ____:
                    right = mid

            __ g[i][left] >= 0:
                _____

            ans += left + 1 __ g[i][right] >= 0 ____ right + 1

        r.. ans
