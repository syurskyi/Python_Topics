"""
REF: https://leetcode.com/problems/game-of-life/discuss/73223

lives < 2       => 1 -> 0
lives == 2 or 3 => 1 -> 1
lives > 3       => 1 -> 0
lives == 3      => 0 -> 1
"""


class Solution:
    """
    Use bits to save the status in next round
    """
    ___ gameOfLife(self, board
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        __ not board or not board[0]:
            r_

        m, n = le.(board), le.(board[0])

        for x in range(m
            for y in range(n
                lives = self.get_live_neibs(board, x, y)

                __ board[x][y] __ 1 and lives in (2, 3
                    board[x][y] = 3
                ____ board[x][y] __ 0 and lives __ 3:
                    board[x][y] = 2

        for x in range(m
            for y in range(n
                board[x][y] >>= 1

    ___ get_live_neibs(self, board, x, y
        cnt = 0
        m, n = le.(board), le.(board[0])

        for dx in (-1, 0, 1
            for dy in (-1, 0, 1
                __ dx __ 0 and dy __ 0:
                    continue

                _x = x + dx
                _y = y + dy

                __ not (0 <= _x < m and 0 <= _y < n
                    continue

                cnt += board[_x][_y] & 1

        r_ cnt


class Solution:
    """
    Not in-place solution
    """
    ___ gameOfLife(self, board
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        __ not board or not board[0]:
            r_

        m, n = le.(board), le.(board[0])
        ans = [[0] * n for _ in range(m)]

        for x in range(m
            for y in range(n
                lives = self.get_live_neibs(board, x, y)
                ans[x][y] = board[x][y]

                __ board[x][y] __ 1 and lives < 2:
                    ans[x][y] = 0
                ____ board[x][y] __ 1 and lives in (2, 3
                    ans[x][y] = 1
                ____ board[x][y] __ 1 and lives > 3:
                    ans[x][y] = 0
                ____ board[x][y] __ 0 and lives __ 3:
                    ans[x][y] = 1

        # return ans

        # hacking for in-place
        for x in range(m
            board[x][:] = ans[x][:]

    ___ get_live_neibs(self, board, x, y
        cnt = 0
        m, n = le.(board), le.(board[0])

        for dx in (-1, 0, 1
            for dy in (-1, 0, 1
                __ dx __ 0 and dy __ 0:
                    continue

                _x = x + dx
                _y = y + dy

                __ not (
                    0 <= _x < m and
                    0 <= _y < n and
                    board[_x][_y] __ 1

                    continue

                cnt += 1

        r_ cnt
