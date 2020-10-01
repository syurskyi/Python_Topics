# Surrounded Regions
# Question: Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# For example:
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
# X X X X
# X X X X
# X X X X
# X O X X
# Solutions:


______ collections
c_ Solution:
    ___ solve(, board):
        __ board __   # list:
            r_   # list
        lineNum _ le.(board)
        colNum _ le.(board[0])
        queue _ collections.deque()
        visited _ [[F.. ___ j __ ra..(colNum)] ___ i __ ra..(lineNum)]
        ___ i __ ra..(colNum):
            __ board[0][i] __ 'O':
                queue.ap..((0, i))
            __ board[lineNum-1][i] __ 'O':
                queue.ap..((lineNum - 1, i))
        ___ i __ ra..(1, lineNum - 1):
            __ board[i][0] __ 'O':
                queue.ap..((i, 0))
            __ board[i][colNum-1] __ 'O':
                queue.ap..((i, colNum - 1))
        w___ queue:
            t _ queue.popleft()
            __ board[t[0]][t[1]] __ 'O': board[t[0]][t[1]] _ '$'
            visited[t[0]][t[1]] _ T..
            __ t[0] + 1 < lineNum an. board[t[0] + 1][t[1]] __ 'O' an. visited[t[0] + 1][t[1]] __ F..:
                queue.ap..((t[0] + 1, t[1]))
            __ t[0] - 1 >_ 0 an. board[t[0] - 1][t[1]] __ 'O' an. visited[t[0] - 1][t[1]] __ F..:
                queue.ap..((t[0] - 1, t[1]))
            __ t[1] + 1 < colNum an. board[t[0]][t[1] + 1] __ 'O' an. visited[t[0]][t[1] + 1] __ F..:
                queue.ap..((t[0], t[1] + 1))
            __ t[1] - 1 >_ 0 an. board[t[0]][t[1] - 1] __ 'O' an. visited[t[0]][t[1] - 1] __ F..:
                queue.ap..((t[0], t[1] - 1))
        ___ i __ ra..(lineNum):
            ___ j __ ra..(colNum):
                __ board[i][j] __ 'O':
                    board[i][j] _ 'X'
                __ board[i][j] __ '$':
                    board[i][j] _ 'O'
        r_ board


Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])