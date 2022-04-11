'''
Created on Jun 6, 2018

@author: tongq
'''
c_ Solution(o..
    ___ isValidSudoku  board
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ___ i __ r..(9
            hashset s..()
            ___ j __ r..(9
                __ board[i][j] __ hashset:
                    r.. F..
                __ board[i][j] != '.':
                    hashset.add(board[i][j])
        ___ j __ r..(9
            hashset s..()
            ___ i __ r..(9
                __ board[i][j] __ hashset:
                    r.. F..
                __ board[i][j] != '.':
                    hashset.add(board[i][j])
        ___ i0 __ r..(3
            ___ j0 __ r..(3
                hashset s..()
                ___ i __ r..(i0*3, i0*3+3
                    ___ j __ r..(j0*3, j0*3+3
                        __ board[i][j] __ hashset:
                            r.. F..
                        __ board[i][j] != '.':
                            hashset.add(board[i][j])
        r.. T..
