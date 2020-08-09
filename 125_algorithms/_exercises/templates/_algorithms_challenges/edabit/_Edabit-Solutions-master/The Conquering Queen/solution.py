___ can_capture(queens
    r_ row_or_column_capture(queens) or diagonal_capture(queens)


___ row_or_column_capture(queens
    r_  queens[0][0] __ queens[1][0] or queens[0][1] __ queens[1][1]


___ diagonal_capture(queens
    diff1 = ord(queens[0][0]) - ord(queens[1][0])
    diff2 = ord(queens[0][1]) - ord(queens[1][1])
    r_ abs(diff1) __ abs(diff2)
