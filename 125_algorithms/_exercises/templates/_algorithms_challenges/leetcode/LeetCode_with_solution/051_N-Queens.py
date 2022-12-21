c_ Solution o..
    ___ solveNQueens  n
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # recusive
        __ n __ 0:
            r_ 0
        res =    # list
        board = [['.'] * n ___ t __ r.. n)]
        do_solveNQueens(res, board, n)
        r_ res

    ___ do_solveNQueens  res, board, num
        __ num __ 0:
            res.append([''.join(t) ___ t __ board])
            r_
        ls = l.. board)
        pos = ls - num
        check = [T..] * ls
        ___ i __ r.. pos
            ___ j __ r.. ls
                __ board[i][j] __ 'Q':
                    check[j] = F..
                    step = pos - i
                    __ j + step < ls:
                        check[j + step] = F..
                    __ j - step >= 0:
                        check[j - step] = F..
                    break
        ___ j __ r.. ls
            __ check[j]:
                board[pos][j] = 'Q'
                do_solveNQueens(res, board, num - 1)
                board[pos][j] = '.'


__ ____ __ ____
    # begin
    s  ?
    print s.solveNQueens(4)