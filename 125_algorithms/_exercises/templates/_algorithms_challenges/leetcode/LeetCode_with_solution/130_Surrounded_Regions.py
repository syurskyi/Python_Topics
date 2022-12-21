c_ Solution o..
    ___ solve  board
        # https://discuss.leetcode.com/topic/22503/some-tips-for-python-code
        __ n.. board:
            r_
        height, width = l.. board), l.. board[0])
        leakWall = buildLeakWall(board)
        w.. leakWall:
            i, j = leakWall.pop()
            __ 0 <= i < height a.. 0 <= j < width:
                __ board[i][j] __ "O":
                    board[i][j] = "S"
                    leakWall += (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
        ___ i __ r.. height
            ___ j __ r.. width
                board[i][j] = "O" __ board[i][j] __ "S" ____ "X"

    ___ buildLeakWall  board
        leakWall, height, width =    # list, l.. board), l.. board[0])
        ___ i __ r.. height
            __ board[i][0] __ "O":
                leakWall.append((i, 0))
            __ board[i][width - 1] __ "O":
                leakWall.append((i, width - 1))
        ___ j __ r.. width
            __ board[0][j] __ "O":
                leakWall.append((0, j))
            __ board[height - 1][j] __ "O":
                leakWall.append((height - 1, j))
        r_ leakWall

    # def solve(self, board):
    #     # https://leetcode.com/problems/surrounded-regions/
    #     if not any(board): return
    #
    #     height, width = len(board), len(board[0])
    #     save = [ij for k in range(height + width) for ij in ((0, k), (height - 1, k), (k, 0), (k, width - 1))]
    #     while save:
    #         i, j = save.pop()
    #         if 0 <= i < height and 0 <= j < width and board[i][j] == 'O':
    #             board[i][j] = 'S'
    #             save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
    #     board[:] = [['XO'[c == 'S'] for c in row] for row in board]


