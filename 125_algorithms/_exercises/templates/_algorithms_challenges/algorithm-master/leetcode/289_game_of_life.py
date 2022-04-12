"""
REF: https://leetcode.com/problems/game-of-life/discuss/73223

lives < 2       => 1 -> 0
lives == 2 or 3 => 1 -> 1
lives > 3       => 1 -> 0
lives == 3      => 0 -> 1
"""


c_ Solution:
    """
    Use bits to save the status in next round
    """
    ___ gameOfLife  board
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        __ n.. board o. n.. board[0]:
            r..

        m, n l..(board), l..(board 0

        ___ x __ r..(m
            ___ y __ r..(n
                lives get_live_neibs(board, x, y)

                __ board[x][y] __ 1 a.. lives __ (2, 3
                    board[x][y] 3
                ____ board[x][y] __ 0 a.. lives __ 3:
                    board[x][y] 2

        ___ x __ r..(m
            ___ y __ r..(n
                board[x][y] >>= 1

    ___ get_live_neibs  board, x, y
        cnt 0
        m, n l..(board), l..(board 0

        ___ dx __ (-1, 0, 1
            ___ dy __ (-1, 0, 1
                __ dx __ 0 a.. dy __ 0:
                    _____

                _x x + dx
                _y y + dy

                __ n.. (0 <_ _x < m a.. 0 <_ _y < n
                    _____

                cnt += board[_x][_y] & 1

        r.. cnt


c_ Solution:
    """
    Not in-place solution
    """
    ___ gameOfLife  board
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        __ n.. board o. n.. board[0]:
            r..

        m, n l..(board), l..(board 0
        ans [[0] * n ___ _ __ r..(m)]

        ___ x __ r..(m
            ___ y __ r..(n
                lives get_live_neibs(board, x, y)
                ans[x][y] board[x][y]

                __ board[x][y] __ 1 a.. lives < 2:
                    ans[x][y] 0
                ____ board[x][y] __ 1 a.. lives __ (2, 3
                    ans[x][y] 1
                ____ board[x][y] __ 1 a.. lives > 3:
                    ans[x][y] 0
                ____ board[x][y] __ 0 a.. lives __ 3:
                    ans[x][y] 1

        # return ans

        # hacking for in-place
        ___ x __ r..(m
            board[x] |  = ans[x] |

    ___ get_live_neibs  board, x, y
        cnt 0
        m, n l..(board), l..(board 0

        ___ dx __ (-1, 0, 1
            ___ dy __ (-1, 0, 1
                __ dx __ 0 a.. dy __ 0:
                    _____

                _x x + dx
                _y y + dy

                __ n.. (
                    0 <_ _x < m a..
                    0 <_ _y < n a..
                    board[_x][_y] __ 1

                    _____

                cnt += 1

        r.. cnt
