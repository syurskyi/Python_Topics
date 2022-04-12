___ can_capture(queens
    r.. row_or_column_capture(queens) o. diagonal_capture(queens)


___ row_or_column_capture(queens
    r..  queens 0 0  __ queens[1][0] o. queens[0][1] __ queens[1][1]


___ diagonal_capture(queens
    diff1  o..(queens 0 0 ) - o..(queens[1] 0
    diff2  o..(queens[0][1]) - o..(queens[1][1])
    r.. a..(diff1) __ a..(diff2)
