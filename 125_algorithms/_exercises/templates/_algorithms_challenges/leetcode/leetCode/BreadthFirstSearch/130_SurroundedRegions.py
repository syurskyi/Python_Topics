#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ solve  board
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        __ n.. board:
            r_
        m_rows = l..(board)
        n_cols = l..(board[0])
        __ m_rows <= 2 or n_cols <= 2:
            r_

        ___ row __ r..(m_rows
            board[row] = list(board[row])

        # Search from the first and last row
        ___ i __ [0, m_rows-1]:
            ___ j __ r..(n_cols
                __ board[i][j] __ "O":
                    self.breadth_first_search(i, j, board)

        # Search from the first and last column
        ___ j __ [0, n_cols-1]:
            ___ i __ r..(m_rows
                __ board[i][j] __ "O":
                    self.breadth_first_search(i, j, board)

        # Make all the O surrounded by X to be X
        ___ i __ r..(m_rows
            ___ j __ r..(n_cols
                __ board[i][j] __ "O":
                    board[i][j] = "X"
                __ board[i][j] __ "#":
                    board[i][j] = "O"
            board[i] = "".join(board[i])

    """
    Mark all the Os can be arrived from outside row(column) to be '#'
    And return one O node's adjacent O nodes
    """
    ___ set_adjacency  row, col, board
        board[row][col] = "#"
        adjacency_node   # list
        m_rows = l..(board)
        n_cols = l..(board[0])
        __ row - 1 >= 0 a.. board[row-1][col] __ "O":
            board[row-1][col] = "#"
            adjacency_node.a.. [row-1, col])
        __ row + 1 < m_rows a.. board[row+1][col] __ "O":
            board[row+1][col] = "#"
            adjacency_node.a.. [row+1, col])
        __ col - 1 >= 0 a.. board[row][col-1] __ "O":
            board[row][col-1] = "#"
            adjacency_node.a.. [row, col-1])
        __ col + 1 < n_cols a.. board[row][col+1] __ "O":
            board[row][col+1] = "#"
            adjacency_node.a.. [row, col+1])
        r_ adjacency_node

    # Do BFS to every out border O ndoe.
    ___ breadth_first_search  row, col, board
        adjacency_nodes = self.set_adjacency(row, col, board)
        adjacency_record   # list
        _____ adjacency_nodes:
            ___ node __ adjacency_nodes:
                adjacency_record.e..(
                    self.set_adjacency(node[0], node[1], board))
            adjacency_nodes = adjacency_record
            adjacency_record   # list
"""
[]
["XXX", "XOX", "XXX"]
["OOX", "XOX", "OXX"]
["XXXX", "XOOX", "XXOX", "XOXX"]
"""
