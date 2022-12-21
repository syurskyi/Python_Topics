#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ exist  board, word
        __ n.. board and word:
            r_ False
        __ n.. word:
            r_ True

        m_rows = l..(board)
        n_cols = l..(board[0])
        ___ row __ r..(m_rows
            ___ col __ r..(n_cols
                __ board[row][col] __ word[0]:
                    board[row][col] = "*"
                    __ (self.exist_adjacent(
                            [row, col],
                            word[1:],
                            board)):
                        r_ True
                    # Backtracking here
                    board[row][col] = word[0]
        r_ False

    ___ exist_adjacent  cur_pos, next_str, board
        # Find all the characters in word.
        __ n.. next_str:
            r_ True

        adj_pos = self.adj_pos_lists(cur_pos, board)
        # No adjancent position can be used.
        __ n.. adj_pos:
            r_ False

        # For every adjacent position, find out whether it contains
        # the first character in the word or not.
        # If matches, then resursively check the other characters in word.
        ___ pos __ adj_pos:
            row = pos[0]
            col = pos[1]
            __ board[row][col] __ next_str[0]:
                board[row][col] = "*"
                __ (self.exist_adjacent(
                        [row, col],
                        next_str[1:],
                        board)):
                    r_ True
                # Backtracking here
                board[row][col] = next_str[0]

        r_ False

    # Find the adjacent position around cur_pos
    ___ adj_pos_lists  cur_pos, board
        m_rows = l..(board)
        n_cols = l..(board[0])
        row = cur_pos[0]
        col = cur_pos[1]
        adj_list   # list
        __ row - 1 >= 0:
            adj_list.append([row - 1, col])
        __ row + 1 < m_rows:
            adj_list.append([row + 1, col])
        __ col - 1 >= 0:
            adj_list.append([row, col - 1])
        __ col + 1 < n_cols:
            adj_list.append([row, col + 1])
        r_ adj_list

"""
[]
""
[]
"as"
["abce","sfcs", "adee"]
"abcced"
["abce","sfcs", "adee"]
"abcb"
["ABCE","SFES","ADEE"]
"ABCESEEEFSAD"
"""
