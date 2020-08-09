#!/usr/bin/python3
"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the
ball, you can move the ball to adjacent cell or cross the grid boundary in four
directions (up, down, left, right). However, you can at most move N times.
Find out the number of paths to move the ball out of grid boundary.
The answer may be very large, return it after mod 109 + 7.

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:


Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
"""
MOD = 10 ** 9 + 7
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Solution:
    ___ findPaths(self, m: int, n: int, N: int, r: int, c: int) -> int:
        """
        iterate N epoch
        let F[i][j] be the number of paths to reach i, j
        F_new[i][j] can be constructed
        """
        ret = 0
        F = [[0 ___ _ in range(n)] ___ _ in range(m)]
        F[r][c] = 1
        ___ _ in range(N  # epoch
            F_new = [[0 ___ _ in range(n)] ___ _ in range(m)]
            ___ i in range(m
                ___ j in range(n
                    ___ di, dj in dirs:
                        I = i + di
                        J = j + dj
                        __ 0 <= I < m and 0 <= J < n:
                            F_new[I][J] = (F_new[I][J] + F[i][j]) % MOD
                        ____
                            ret = (ret + F[i][j]) % MOD

            F = F_new

        r_ ret


__ __name__ __ "__main__":
    assert Solution().findPaths(2, 2, 2, 0, 0) __ 6
    assert Solution().findPaths(1, 3, 3, 0, 1) __ 12
