#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ isValidSudoku  board
        # check for rows
        ___ row __ board:
            row_hash _ # dict
            ___ c __ row:
                __ c != "." a.. c __ row_hash:
                    r_ False
                row_hash[c] = 1

        # check for cols
        ___ i __ r..(9
            col_hash _ # dict
            ___ row __ board:
                __ row[i] != "." a.. row[i] __ col_hash:
                    r_ False
                col_hash[row[i]] = 1

        # check for panel
        ___ i __ r..(0, 9, 3
            ___ j __ r..(0, 9, 3
                count = 0
                panel_hash _ # dict
                _____(count < 9
                    c = board[i + count // 3][j + count % 3]
                    count += 1
                    __ c != "." a.. c __ panel_hash:
                        r_ False
                    panel_hash[c] = 1

        r_ True

"""
["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
"""
