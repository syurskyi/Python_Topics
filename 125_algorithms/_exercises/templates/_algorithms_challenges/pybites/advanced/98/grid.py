import re
DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


___ print_sequence_route(grid, start_coordinates_ N..
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""

    
    
    matrix = []
    for i,line in enumerate(grid.splitlines()):
        __ i % 2 == 1:
            values = list(map(int,re.split(r'\D+',line)))
            __ START_VALUE in values:
                start_row = len(matrix)
                start_col = values.index(START_VALUE)
            matrix.append(values)
    

    length = len(matrix)

    goal = length**2
    current_row,current_col = start_row,start_col
    current_value = START_VALUE 

    previous_direction = None

    
    print(current_value,end=' ')
    while current_value != goal:
        directions = ((current_row + 1,current_col,DOWN),(current_row - 1,current_col,UP),(current_row,current_col + 1,RIGHT),(current_row,current_col -1,LEFT))


        for neighbor_x,neighbor_y,direction in directions:
            __ 0 <= neighbor_x < length and 0 <= neighbor_y < length:
                __ matrix[neighbor_x][neighbor_y] == current_value + 1:
                    __ previous_direction is not None and direction != previous_direction:
                        print(direction)
                        previous_direction = direction
                    elif previous_direction is None:
                        previous_direction = direction
                    print(current_value + 1,end=' ')

                    break

        current_row,current_col = neighbor_x,neighbor_y
        current_value += 1











__ __name__ == "__main__":


    small_grid = """
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




