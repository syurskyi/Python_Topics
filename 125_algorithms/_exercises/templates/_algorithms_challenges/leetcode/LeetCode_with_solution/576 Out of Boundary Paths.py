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
        F = [[0 ___ _ __ r..(n)] ___ _ __ r..(m)]
        F[r][c] = 1
        ___ _ __ r..(N):  # epoch
            F_new = [[0 ___ _ __ r..(n)] ___ _ __ r..(m)]
            ___ i __ r..(m):
                ___ j __ r..(n):
                    ___ di, dj __ dirs:
                        I = i + di
                        J = j + dj
                        __ 0 <= I < m a.. 0 <= J < n:
                            F_new[I][J] = (F_new[I][J] + F[i][j]) % MOD
                        ____:
                            ret = (ret + F[i][j]) % MOD

            F = F_new

        r.. ret


__ __name__ __ "__main__":
    ... Solution().findPaths(2, 2, 2, 0, 0) __ 6
    ... Solution().findPaths(1, 3, 3, 0, 1) __ 12
