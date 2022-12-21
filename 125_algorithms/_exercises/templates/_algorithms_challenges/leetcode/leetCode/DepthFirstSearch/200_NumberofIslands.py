#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ numIslands  grid
        __ n.. grid:
            r_ 0
        island_counts = 0
        self.m_rows = l..(grid)
        self.n_cols = l..(grid[0])
        self.grid = grid

        island_counts = 0
        ___ i __ r..(self.m_rows
            ___ j __ r..(self.n_cols
                __ grid[i][j] __ "1":
                    island_counts += 1
                    self.merge_surround(i, j)

        r_ island_counts

    # Depth First Search
    # Merge all the adjacent islands to one island.
    ___ merge_surround  i, j
        __ self.grid[i][j] __ "1" or self.grid[i][j] __ "#":
            __ i+1 < self.m_rows and self.grid[i+1][j] __ "1":
                self.grid[i+1][j] = "#"
                self.merge_surround(i+1, j)
            __ j+1 < self.n_cols and self.grid[i][j+1] __ "1":
                self.grid[i][j+1] = "#"
                self.merge_surround(i, j+1)
            __ i-1 >= 0 and self.grid[i-1][j] __ "1":
                self.grid[i-1][j] = "#"
                self.merge_surround(i-1, j)
            __ j-1 >= 0 and self.grid[i][j-1] __ "1":
                self.grid[i][j-1] = "#"
                self.merge_surround(i, j-1)
        r_

"""
["1"]
["111","010","111"]
["111", "100", "101", "111"]
["11110", "11010", "11000", "00000"]
["11000", "11000", "00100", "00011"]
"""
