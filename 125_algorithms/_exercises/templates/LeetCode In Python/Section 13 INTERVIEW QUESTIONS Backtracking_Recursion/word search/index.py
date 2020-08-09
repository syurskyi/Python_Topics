c_ Solution:
    dx _ [0, 0, -1, 1]
    dy _ [1, -1, 0, 0]

    ___ solution(, board, word, x, y, cur
        __(x < 0 or x >_ le.(board) or y < 0 or y >_ le.(board[x]) or board[x][y] __ ' '
            r_ False
        cur +_ board[x][y]

        __(le.(cur) > le.(word)):
            r_ False
        __(cur[le.(cur)-1] !_ word[le.(cur)-1]
            r_ False
        __(cur __ word
            r_ T..

        temp _ board[x][y]
        board[x][y] _ ' '

        ___ i __ ra..(4
            __(.solution(board, word, x+.dx[i], y+.dy[i], cur)):
                r_ T..

        board[x][y] _ temp
        r_ False

    ___ exist(, board: L..[L..[st.]], word: st.) -> bool:
        __(le.(word) __ 0
            r_ T..
        n _ le.(board)
        ___ i __ ra..(n
            m _ le.(board[i])
            ___ j __ ra..(m
                __(word[0] __ board[i][j] and .solution(board, word, i, j, "")):
                    r_ T..
        r_ False
