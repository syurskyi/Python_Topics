class Solution:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    ___ solution(self, board, word, x, y, cur
        __(x < 0 or x >= le.(board) or y < 0 or y >= le.(board[x]) or board[x][y] __ ' '
            r_ False
        cur += board[x][y]

        __(le.(cur) > le.(word)):
            r_ False
        __(cur[le.(cur)-1] != word[le.(cur)-1]
            r_ False
        __(cur __ word
            r_ True

        temp = board[x][y]
        board[x][y] = ' '

        ___ i __ ra..(4
            __(self.solution(board, word, x+self.dx[i], y+self.dy[i], cur)):
                r_ True

        board[x][y] = temp
        r_ False

    ___ exist(self, board: List[List[str]], word: str) -> bool:
        __(le.(word) __ 0
            r_ True
        n = le.(board)
        ___ i __ ra..(n
            m = le.(board[i])
            ___ j __ ra..(m
                __(word[0] __ board[i][j] and self.solution(board, word, i, j, "")):
                    r_ True
        r_ False
