_______ __
DOWN, UP, LEFT, RIGHT '⇓', '⇑', '⇐', '⇒'
START_VALUE 1


___ print_sequence_route(grid, start_coordinates_ N..
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""

    
    
    matrix    # list
    ___ i,line __ e..(grid.s..
        __ i % 2 __ 1:
            values l.. m..(i..,__.s.. _ \D+',line)))
            __ START_VALUE __ values:
                start_row l..(matrix)
                start_col values.i.. START_VALUE)
            matrix.a..(values)
    

    length l..(matrix)

    goal length**2
    current_row,current_col start_row,start_col
    current_value START_VALUE

    previous_direction N..

    
    print(current_value,end=' ')
    w.... current_value !_ goal:
        directions ((current_row + 1,current_col,DOWN),(current_row - 1,current_col,UP),(current_row,current_col + 1,RIGHT),(current_row,current_col -1,LEFT


        ___ neighbor_x,neighbor_y,direction __ directions:
            __ 0 <_ neighbor_x < length a.. 0 <_ neighbor_y < length:
                __ matrix[neighbor_x][neighbor_y] __ current_value + 1:
                    __ previous_direction __ n.. N.. a.. direction !_ previous_direction:
                        print(direction)
                        previous_direction direction
                    ____ previous_direction __ N..
                        previous_direction direction
                    print(current_value + 1,end=' ')

                    _____

        current_row,current_col neighbor_x,neighbor_y
        current_value += 1











__ _______ __ _______


    small_grid """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13"""


    print_sequence_route(small_grid)




